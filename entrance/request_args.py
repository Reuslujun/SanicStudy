from sanic import Sanic,json
from sanic.log import logger


app = Sanic('app')


@app.middleware('request')
async def before_request(request):
    
    logger.info(f'args: {request.args}')



@app.route('/getArgs')
async def get_args(request):
    request_args  = request.args #用户定义的参数直接通过args来获取
    return json(request_args)


if __name__ == '__main__':
    app.run('localhost',8044)