
# shell中若是想要给某个变量赋值，则推荐使用``反引号
# 如果包含有多个pid，那么shell脚本会挨个kill
# shell中一般使用''单引号表示内容不会被替换，而使用""双引号则其中的内容会替换,直接使用$xxx可以获取变量值
# 建议在 [] 括号内的变量左右放置空格。这也是一种良好的编程习惯。
# 在shell中，-ge 是一个比较运算符，表示"大于等于"
# exit 0 来指示成功的退出
# grep -v grep 这里的-v表示的是反选，其本质是过滤出不包含grep命令的进程
# 这里的awk是一个文本处理工具，'{print $2}' 是AWK脚本的一部分，包含在单引号内。这个脚本告诉AWK执行以下操作：
# print 表示打印输出。
# $2 表示当前处理的文本行中的第二个字段（列）。


python_pid=`ps -ef|grep -E 'python'|grep -v grep|awk '{print $2}'`


if [ "$python_pid" == "" ];then
    echo "no need to kill"
    exit 0;
else
    kill $python_pid
    echo "many killed"
fi



