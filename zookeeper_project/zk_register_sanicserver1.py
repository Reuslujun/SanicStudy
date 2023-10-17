from kazoo.client import KazooClient
import json

from kazoo.exceptions import NodeExistsError


def register():
    '''
    将sanic_server服务1注册到zk
    :return:
    '''
    zk = KazooClient(hosts=' 0.0.0.0:2181,0.0.0.0:2182,0.0.0.0:2183')
    zk.start()

    server_data = ['0.0.0.0:6666', '0.0.0.0:7777']
    # TODO 这里就是注册到zk上的地址
    node_path = 'lujun/zk/server_list'
    try:
        # 尝试创建节点
        # TODO 注意这里是makepath=True，表示递归注册
        # zk.create(node_path, value=json.dumps(server_data).encode('utf-8'), makepath=True)
        # TODO 这里是就行相关的修改操作
        # TODO 但凡是要注册到zk，就必须json序列化
        zk.set(node_path, value=json.dumps(server_data).encode('utf-8'),)
        print(f"Node {node_path} created successfully.")

    except NodeExistsError:
        # 节点已经存在，可以执行更新操作或其他逻辑
        print(f"Node {node_path} already exists. Performing update or other logic.")
    zk.stop()

if __name__ == '__main__':
    register()