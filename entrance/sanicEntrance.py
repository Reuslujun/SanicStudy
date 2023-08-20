from sanic import Sanic
from sanic.response import text

db_config ={
    'name':'lujun',
    'address':'0.0.0.0'
}


app = Sanic("First",config=db_config)



app.config.update_config(db_config)



@app.get("/lujun")
async def hello_world(request):

    sanic_app = app.get_app("First")
    
    print("address: ",sanic_app.get_address)
    return text("Hello, world.")


if __name__ == '__main__':
    app.run(host="localhost",port=8080)