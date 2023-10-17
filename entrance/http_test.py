import requests


param = {
    'name':'lujun',
    'age':25
}


response = requests.get('http://localhost:8044/getArgs',params=param)