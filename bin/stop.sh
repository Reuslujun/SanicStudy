#!/bin/sh

base=`dirname $0`/.. # 获取当前脚本文件所在目录的上一级目录


echo "lllll ${base}"
LOOPS=0 #记录当前重试的次数
while (true);
do
    python_pid=`ps -ef|grep -E 'python'|grep -v grep |awk '{print $2}'`

    if [ "$python_pid" == "" ]; then #查找运行中的python服务进程，若无则直接删除记录进程ID的文件和日志，避免遗留的记录数据对后续脚本执行产生干扰
        echo "kill python server success!"
        # rm -f ${base}/python_server.pid
        # rm -f ${base}/python_server.log
        exit 0; #没必要的时候就直接退出
    else 
        echo "${appName} try to kill python server" # 使用kill命令结束进程ID为`python_pid`的进程
        kill $python_pid
    fi

    if [ $LOOPS -ge 5 ]; then # 判断当前脚本执行以来发出的结束信号次数是否超过5次，若是超过了则无法正常响应，强制结束进程
        echo "${appName} kill failed more than five times, then kill -9"
        kill -9 $python_pid
    fi

    let LOOPS=LOOPS+1 #重试次数+1
    sleep 1 #进程休眠1秒，防止其抢占CPU资源
done


#  python_pid=`ps -ef|grep -E 'odapr_server'|grep -v grep |awk '{print $2}'`这句代码的作用
# 使用`ps`命令查找所有包含字符串'odapr_server'的进程，然后通过`grep`过滤出不含有"grep"的结果行，最后通过`awk`命令从结果行中提取出进程ID，赋值给变量`python_pid`