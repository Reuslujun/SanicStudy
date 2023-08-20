from sanic import Sanic,text

app = Sanic('lujun')



async def listen_use(app):
    return 25


@app.route("/lujun")
async def listen_before(request):
    print(request.args)
    return text("25")


@app.middleware("request")
async def middle_listener(request):
    age = await listen_use(request)
    request.ctx.name = "lujun"
    print("age before: ",age)
    

   
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8066,workers=2)

    