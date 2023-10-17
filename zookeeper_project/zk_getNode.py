from kazoo.client import KazooClient

def get_registered_nodes():
    '''
    获取已注册的节点
    :return: 节点列表
    '''
    zk = KazooClient(hosts='0.0.0.0:2181,0.0.0.0:2182,0.0.0.0:2183/lujun/zk')
    zk.start()

    node_path = 'server_list'  # 指定你要查询的节点路径
    registered_nodes = []

    if zk.exists(node_path):
        # 获取节点的数据
        data, _ = zk.get(node_path)
        registered_nodes.append((node_path, data.decode('utf-8')))

        # 获取节点下的子节点
        # TODO 这里的get_children就是在传入的指定node_path目录下查看是否有子节点
        # TODO 这里的指定node_path目录是server_list，其下并没有子节点
        children = zk.get_children(node_path)
        for child in children:
            child_path = f"{node_path}/{child}"
            # TODO 这里的返回的是一个tuple,node 然后这里的node节点信息可不用
            child_data, _ = zk.get(child_path)
            registered_nodes.append((child_path, child_data.decode('utf-8')))

    zk.stop()
    return registered_nodes

if __name__ == '__main__':
    nodes = get_registered_nodes()
    for node_path, node_data in nodes:
        print(f"Node Path: {node_path}, Node Data: {node_data}")
