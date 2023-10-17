from sanic  import Sanic,response
import setproctitle



service_name = 'sanic_lujun'
setproctitle.setproctitle(service_name)


app = Sanic('lll')



@app.get('/getinfo')
async def getInfo (request):
    
    return response.text("lll")


if __name__ == '__main__':
    app.run('localhost',8099)
