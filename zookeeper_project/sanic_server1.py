from  sanic import Sanic,response

app = Sanic("lujun")

@app.route("/name")
def getName(request):
    return  response.text("hello ,lujun")


if __name__ == '__main__':
    app.run('localhost',6666)