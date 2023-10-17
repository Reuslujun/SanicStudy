from  sanic import Sanic,response

app = Sanic("lujun")

@app.route("/age")
def getName(request):
    return  response.text("I am 25 years old")


if __name__ == '__main__':
    app.run('localhost',7777)