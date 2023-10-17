"""
这个代码主要是用来尝试直接根据zk的地址能不能获取得到注册上去的服务的IP：端口
"""

from kazoo.client import KazooClient
import json


def get_server_list(host):
    zk = KazooClient(hosts=host)
    zk.start()
    # TODO 获取当前路径下 server_list这个节点的信息，返回 tuple,node
    server_list, _ = zk.get('server_list')

    return json.loads(server_list)