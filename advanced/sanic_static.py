from sanic import Sanic,response


app = Sanic("lujun")

class Test:
    @staticmethod
    def add_num(x,y):
        return x+y
    

@app.route("/add")
async def get_num(request):
    num = Test.add_num(8,9)
    return response.text(f"num is: {num}")

if __name__ == '__main__':
    app.run('0.0.0.0',8099)