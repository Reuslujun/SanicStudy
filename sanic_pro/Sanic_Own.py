from HTTPServer import  HTTPServer
from  typing import Optional,Text

class SanicOwn:
    def __init__(self,name):
        self.name = name
        self.actors =[]
        # TODO 这里一定要实例化HTTPServer()，否则调用的时候他只是一个类，而不是实例对象
        self.server = HTTPServer(self.name)

    def register_actor(self, handler,  method_name,verb):
        '''
        不断的往列表中添加actor响应
        :param actor:
        :return:
        '''
        # TODO 这里使用的append()方法是将这个元组一起打包,之后就直接使用 *actor参数来解包，但是记住参数要一一对应
        self.actors.append((handler,method_name,verb))


    def register_listener(self,handler,event):
        '''

        :param handler:
        :param event:
        :return:
        '''

        self.server.register_listener(handler=handler,event=event)


    def run_sanic(self,host,port,workers):
        '''
        根据指定给的host 和 port 让程序运行
        :param host:
        :param port:
        :return:
        '''


        # TODO仔细一点，这里要指定sanic服务的run
        self.server.run(host=host,port=port,workers=workers)

    def _run_worker(self):
        # TODO 这里循环actor是因为要注册多个api的接口
        # TODO 这里首先将多个actor进行注册，之后再统一的调用，这就是应用来工厂设计模式的思想来将多个操作抽象化为一个actor
        # TODO 然后这里先注册，再统一调用，就用到了依赖注入的设计模式思想
        for actor in self.actors:
            # TODO 这里的 *actor就是python的装包传递，传递进去之后python就会自动解包来参数一一对应
            print("actor: ",actor)
            self.server.register_actor(*actor)






