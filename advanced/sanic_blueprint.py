from sanic import Sanic,Blueprint,response
from sanic.log import logger
import json

app = Sanic('lujun')
bp1 = Blueprint('new_bp','/blueprint1')
bp2 = Blueprint('new_bp_2','/blueprint2')

async def getName(request):
    return "lujun"


async def getAge(request):
    return 25


@bp1.route('/name')
async def printName(request):
    name  = await getName(request)
    return response.text(f'name is: {name}')

@bp1.get('/age')
async def printAge(request):
    age = await getAge(request)
    json_age = {'age':age}
    return response.json(json.dumps(json_age))

@bp1.middleware('request')
async def request_before(request):
    logger.info(f"这是bp1 log")
    print ("print bp1 bp1 bp1")

@bp2.middleware('request')
async def request_before(request):
    logger.info(f"这是bp2 log")
    print ("print bp2 bp2 bp2")


@bp2.route('/name')
async def printName2(request):
    name = await getName(request)
    return response.text(f'name is {name}')


app.blueprint([bp1,bp2])




if __name__ == '__main__':
    app.run('0.0.0.0',8099)