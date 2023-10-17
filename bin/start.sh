#!/bin/sh


# TODO 这里的 $0 表示当前脚本的文件名
# TODO 这里的 dirname 命令表示获取一个文件的父级目录，这里就是获取当前脚本的父级目录
env_path=$(dirname $0)/../../env.sh # 表示获取当前脚本的两级父级目录的路径，并在该路径下找到名为 `env.sh` 的脚本文件


# TODO 这里的[[..]] 在shell中是测试一个条件是否成立，-f是一个测试表达式，用来测试某个路径是否为一个文件
if [[ -f ${env_path} ]]; then #若是env.sh存在，则加载这个环境启动文件
    source ${env_path}  # TODO 这里的source命令就是会执行当前文件
fi

# TODO 这里的 `uname`表示当前操作系统的名称，将这个名称给输出
case "`uname`" in #判断当前操作系统的类型
    Linux)
		bin_abs_path=$(readlink -f $(dirname $0)) # TODO readlink -f 会将 $(dirname $0)获取的父路径转换为绝对路径
		;;
	*)
		bin_abs_path=`cd $(dirname $0); pwd` #TODO 若不是则通过cd切换到当前文件的父路径，并用pwd命令打印出来，这样可保证bin_abs_path变量设置为当前脚本所在目录的完整绝对路径
		;;
esac
echo ${bin_abs_path} # 输出当前脚本的绝对路径
base=${bin_abs_path}/.. # 获取上级目录路径
cd ${base} #切换到上级目录



# `ps -ef`命令用于显示当前系统中正在运行的进程信息；
# `grep -E "odapr_server|skill_config"`命令用于只保留包含字符串"odapr_server"或"skill_config"的行；
# `grep -v grep`命令用于去掉结果中包含字符串"grep"的行（因为之前是通过`grep`命令来过滤结果的）；
# TODO `wc -l`命令用于计算结果中行数，也就是正在运行名为`odapr_server`或`skill_config`的进程数量。wc表示word count，用来统文件信息
procPyNum=`ps -ef | grep -E "odapr_server|skill_config" | grep -v grep | wc -l`
echo "procPyNum:$procPyNum"
if [ $procPyNum -ge 1 ]; # 如果正在运行的进程数大于1，则服务正在运行，无需启动
then
    echo "python tag-classification  is running, no need to start"
    exit 0
else
    cd ${base}
    echo "base is ${base}"
    echo "python: $(which python3)" #输出当前系统中python3的可执行文件的路径，并在其前面加上python
    nohup $(which python3) -u server.py -sf ${base}/config/tag_config.json 1>>${base}/logs/python_server.log 2>&1 & #启动一个python进程并在后台运行，并将运行日志输出到指定文件中
    echo $! > ${base}/logs/python_server.pid # 保存后台生成的进程ID，后面可通过该记录的进程ID杀死该进程
fi

# nohup $(which python3) -u server.py -sf ${base}/config/tag_config.json 1>>${base}/logs/python_server.log 2>&1 & 代码的作用

# - `$(which python3)`命令用于获取当前系统中`python3`可执行文件的绝对路径；
# - `-u`选项表示关闭Python的缓冲区，让程序的运行日志实时输出到文件中；
# TODO nohup命令表示后台运行
# - `server.py`表示要启动的Python服务器的程序文件名；
# - `-sf ${base}/config/tag_config.json`表示程序运行所需要的配置文件；
# - `1>> ${base}/logs/python_server.log`表示将标准输出重定向到指定的日志文件中，`1`表示标准输出流的文件描述符（默认为1），`>>`表示数据追加到日志文件中（而不是覆盖已有的内容）；
# - `2>&1`表示将标准错误输出重定向到与标准输出相同的地方，其中，`2`表示标准错误流的文描述符，`&1`表示重定向到标准输出流中；
# - `&`符号表示将整个命令在后台运行，而不占用当前终端的会话。


#  echo $! > ${base}/logs/python_server.pid 这句代码的作用
# - `$!`表示上一条在后台运行的命令所生成的进程ID，该参数会自动地保存在特殊的Shell变量中；
# - `>`表示将`$!`的值重定向到指定的日志文件中（覆盖原有内容），`>>`表示将值追加到指定文件的末尾；
# - `${base}/logs/python_server.pid`指定了要保存进程ID的文件的路径和文件名。