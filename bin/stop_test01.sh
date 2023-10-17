# TODO 将在运行的进程中的关键字 'python'的进程获取，然后将这个进程给干掉


python_pid=`ps -ef|grep -E 'python' | grep -v grep|awk '{print $2}'`

if [ "${python_pid}" == "" ];then
  echo "no python_server need to kill"
else
  kill  ${python_pid}
fi