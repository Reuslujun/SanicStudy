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
from Sanic_Own import  SanicOwn

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




app = SanicOwn('lujun')
# TODO 在python中，若是函数不带括号，比如这里的init_server，predict_Get 就是函数回调机制，在特定的条件才会执行
# TODO 但是如果函数带上了括号，比如这里的SanicOwn('lujun') 函数就会立刻执行
app.register_listener(init_server, "before_server_start")
app.register_actor(predict_Get, '/api/own/get', ['GET'])
app.register_actor(predict_Post, '/api/own/post', ['POST'])
app._run_worker()


if __name__ == '__main__':
    # TODO 主线程只能是一个sanic的run()，然后在主线程run之前，必须将actor和listener注册完毕
    app.run_sanic('localhost', 8022, workers=1)
