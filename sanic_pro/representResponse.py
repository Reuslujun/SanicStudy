import base64
from typing import  Optional
from  sanic import  Sanic,response

class RepresentResponse:

    def __init__(self,return_code,use_time,data):
        self.return_code =return_code
        self.use_time = use_time
        self.data = data

    # TODO 这里使用response.json来组装返回的内容，因为返回的对象必须是response类型
    # TODO 有时候可以相信自己的想法，不一定得按照公司的安排写
    def to_http_response(self):
        final_code = 200
        json_data = {
            'return_code':self.return_code,
            'use_time': self.use_time,
            'data':self.data
        }

        return response.json(body=json_data,status=final_code)
