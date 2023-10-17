
# 目的：因为项目运行的server.py是和当前文件夹的父目录同级，所以要运行server.py，
# 首先要获取当前文件夹的父目录，再切换上一级，也就是server.py文件的目录
# 第二步骤：根据 ps -ef命令过滤出当前进程中是否有目标服务，如果有则不用启动，如果没有则启动
# 第三步：根据 python server.py运行脚本文件，并且将日志文件写入到logs/python_server.logs文件中
# 第四步：将进程的pid进行保存到logs/python_server.pid

# TODO ${...}就是变量替换，而$(...)就是命令替换，shell会执行其中的命令


# 获取脚本的绝对路径
# TODO $0 获取当前文件的路径(相对或绝对取决于自己的命令)
# TODO dirname 获取这个路径的目录(其不管相对或绝对都是获取目录)
# TODO 这里使用 cd 命令来切换到目标目录，再使用pwd显示绝对路径

script_dir=$(cd "$(dirname $0)" && pwd)
echo "当前shell脚本的父目录的绝对路径:" ${script_dir}

# 因为使用了pwd命令，所以已经获取了绝对路径，dirname命令就是获取此绝对路径的目录
parent_dir=$(dirname $script_dir)
echo  "当前bin文件夹父目录: " ${parent_dir}

echo "python:" $(which python)

# TODO 这里的 1>> 就是将此python程序执行的输出流输出到指定的log文件日志，输出流可以在terminal中，也可在指定文件，这里是追加
# TODO 在后端框架中只有log的内容才会成为python程序执行的输出流输出
# TODO 在shell脚本中，0代表输入，1代表标准输出，2代表标准错误，>表示将标准输出重定向到文件，然后这里的 >> 2个>就是追加的形式
# TODO 这里的 2>&1 中 2代表着错误，这里的&1就是引用1，引用1的位置，表示将2错误输出的内容合并到1的位置，也就是2者输出相同位置
# TODO  最后这里一个&就表示整个脚本在后台执行，不占用当前资源
$(which python) ${parent_dir}/test.py 1>>${parent_dir}/logs/python_server.log 2>&1 &
# TODO $! 获取最后一个在后台运行的进程的进程ID（PID）。它通常用于获取并记录后台任务的PID
# TODO 这里使用 $! > 也只是将最后一个pid重定向到指定的文件，但是要执行还是需要使用echo命令
echo  $! > ${parent_dir}/logs/python_server.pid

# TODO 但凡是获取命名的变量都是使用 `xxx`
procNum=`ps -ef|grep -E "python"| grep -v "grep"|wc -l`
echo  "procNum: " ${procNum}

# TODO  若是这里是用了[ xx ]，那就必须在xx的左右都空一个空格
if [ "$procNum" -ge 1 ];then
  echo "too many"
  exit 0;
fi
