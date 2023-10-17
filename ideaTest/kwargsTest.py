"""
这里就是模仿query的需求，针对输入的文本提取出关键信息，然后传递给下游，下游根据关键的信息来拼接
"""

def do_query(query):
    """
    对输入的文本进行处理
    :param query: 输入的内容
    :return: 返回想要的结果
    """

    count = len(query)
    label_first = query[-1]
    info = {'label':label_first,'length':count}
    name = 'lujun'

    # TODO 如果下游函数指定了使用**kwargs，那就要自己塞变量，自己写好细致化的函数
    query_1 =get_query(name,label=label_first,length=count)
    # TODO 如果函数自己有很多的细致变量，那么自己想简化，就直接**info，python会自动帮忙解包，下游就要写好细致化的参数
    query_2 = get_query_info(name,**info)
    print("query1: ",query_1)
    print("query2: ",query_2)


def get_query(name,**kwargs):
    result = 'name: ' + name + " label: " + kwargs.get('label') + " len: " + str(kwargs.get('length'))
    return result


def get_query_info(name,length,label):
    """
    根据文本的长度和label进行拼接
    :param length: 文本长度
    :param label: 文本标签
    :return:
    """
    result = 'name: '+name+" label: "+label+" len: "+str(length)
    return result

if __name__ == '__main__':
    query = "你好"
    do_query(query=query)