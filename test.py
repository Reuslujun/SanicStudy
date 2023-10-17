from sanic import Sanic,response
import logging
import setproctitle

app = Sanic('name')

# 配置日志记录器
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

@app.route('/name')
def get_name(request):
    logging.info("我在尝试写shell脚本")
    print("我在print")
    return response.text('lujun')

if __name__ == '__main__':
    setproctitle.setproctitle('sanic_shell')  # 设置进程名称
    app.run('localhost', 9999)
