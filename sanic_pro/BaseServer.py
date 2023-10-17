import abc

class BaseServer(abc.ABC):
    def __init__(self,name):
        self.name = name
        # TODO 这里的_init_server()必须带上()，表明是立刻调用的这个函数
        self.server = self._init_server()

    @abc.abstractmethod
    def _init_server(self):
        pass

    @abc.abstractmethod
    def register_actor(self,handler,method,verb):
        pass

    @abc.abstractmethod
    def register_listener(self,handler,event):
        pass


    @abc.abstractmethod
    def run(self,host,port,workers):
        pass