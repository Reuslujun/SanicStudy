
from BaseServer import  BaseServer
from  sanic import  Sanic

class  HTTPServer(BaseServer):
    # TODO 使用快捷键来一次性地继承全部接口
    def __init__(self, name):
        # TODO 这里使用super就是将初始化的内容全部都继承，而下面的就是继承接口
        # TODO 这里若需要继承多少个参数，则统一在 super().__init__()括号中写好
      super().__init__(name)


    def _init_server(self):
        server = Sanic(self.name)
        return server

    def register_actor(self,handler,method,verb):
        self.server.add_route(handler,method,verb)

    def register_listener(self,handler,event):
        self.server.register_listener(handler,event)

    def run(self,host,port,workers):
        self.server.run(host=host,port=port,workers=workers)
