from sanic import Sanic
from sanic import response,json

app = Sanic('lujun')



@app.route('/lujun')
async def index(request):
    # 检查身份验证状态
    print("args: ",request.args)

    return json({'eat':'meat'},status=202)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

# 这段程序中，能否冲request请求中获取