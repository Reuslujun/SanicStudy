# encoding: utf-8
# 核心需求就是练习sanic的register_listener() 和 register_add()方法
# register_add()方法就是主要的核心类，这个类是真正的接口响应,处理请求,register_add(request)
# register_listener()是添加监听器，在方法主进程启动前和主进程启动之后，针对app实例操作,register_listener(app)
# 需求：输入一段文字，给每段文字后面添加上'lujun'字段

# register_add() -> add_string(request) -> 核心的操作
# register_listener() -> init_server(app) -> 在服务起来之前将核心函数Main注册进来
# register_listener() -> warm_up(app) -> 预热丰富，在服务起来之后先执行一下，直接调用add_string


from sanic import Sanic,response
from represent import MainDemo
import json
from representResponse import RepresentResponse
import time

SUCCESS = 0
CACHED = 1
FAILED = 2


def RESPONSE_SUCC(use_time, data):
    response_success = RepresentResponse(return_code=SUCCESS, use_time=use_time, data=data)
    return response_success.to_http_response()


def RESPONSE_CACHED(use_time, data):
    response_cached = RepresentResponse(return_code=CACHED, use_time=use_time, data=data)
    return response_cached.to_http_response()


def RESPONSE_FAILED(use_time):
    response_failed = RepresentResponse(return_code=FAILED, use_time=use_time, data=None)
    return  response_failed.to_http_response()


async def init_server(app):
    '''
    注册核心的主函数
    :param app:
    :return:
    '''
    app.ctx.servicer = MainDemo() # TODO 这里记住是servicer属性


async def predict_Post(request):
    '''
    执行预测的函数
    :param request:
    :return:
    '''
    time_before = time.time()
    try:
        json_name = json.loads(request.body) # TODO 使用json.loads(request.body)来解析POST请求中的JSON数据
        query = json_name.get('name')
    except json.JSONDecodeError:
        use_time_failure = time.time() - time_before
        return  RESPONSE_FAILED(use_time_failure)
    result = request.app.ctx.servicer.add_name(query)
    use_time_success = time.time() - time_before
    return  RESPONSE_SUCC(use_time=use_time_success,data=result) # TODO 查看一下公司的代码是如何封装的response


async def predict_Get(request):
    '''
    执行预测的函数
    :param request:
    :return:
    '''
    query = request.args.get('name') #TODO 如果是get请求的方式，直接使用request.args.get(‘xxx’)获取
    result = request.app.ctx.servicer.add_name(query)
    return  response.text(result)




#TODO，这里的注册必须是全局变量才可以将serivcer实例注册进去,其在服务启动之前才会注册进入sanic
# 在多线程或多进程环境中，Sanic需要确保应用程序的实例化只发生一次。
# 如果你在if __name__ == '__main__':块内实例化应用程序，那么每个进程或线程都会尝试实例化应用程序，这可能会导致冲突。
app = Sanic('lujun')
# TODO add_route()传入的函数是针对路由，所以需要传入request对象
# TODO register_listener() 是针对函数实例进行的监听，所以需要传入app实例
# TODO “before_server_start”就是在server开始之前，所以需要将服务注册进 servicer，后续所有的监听器都是从request中获取app实例
# TODO 对app的任何操作（例如，注册路由/创建蓝图/更新配置等）都必须在if __name__ == '__main__'之前完成，在if __name__ == '__main__'对app的操作只能时app.run
app.register_listener(init_server, "before_server_start")
app.add_route(predict_Post, '/api/name/post', ['post'])
app.add_route(predict_Get,'/api/name/get',['get'])

if __name__ == '__main__':
    app.run('localhost', 8022,workers=3)


# 在多进程或多线程的应用中，如果每个进程或线程都在if __name__ == '__main__':块内实例化Dapr类，这并不会导致冲突，因为每个进程或线程都会有自己的独立的Python解释器实例，它们的内存空间是隔离的。
# 在这种情况下，每个进程或线程会独立地创建和使用Dapr类的实例，互不干扰。

# if __name__ == '__main__':块通常用于确保主程序只在主进程或线程中运行，而不是在派生的子进程或线程中运行。
# 在多进程或多线程的应用中，主程序通常负责创建子进程或子线程，并在每个子进程或子线程中运行相同的代码。
# 每个子进程或子线程都会独立执行主程序，这就是为什么可以在每个子进程或子线程中安全地实例化Dapr类。
#
# 要注意的是，虽然每个进程或线程中的Dapr类实例相互独立，但它们可以共享某些资源，例如共享内存或文件。
# 在这种情况下，需要采取适当的同步和互斥措施，以确保资源的安全访问，以防止竞态条件和数据损坏。
# 但从你提供的代码来看，似乎没有涉及到这种资源共享情况。