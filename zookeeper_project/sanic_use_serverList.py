from sanic import Sanic, response
from zk_getServer_list import get_server_list
import requests

app = Sanic("Reus")


@app.route("/try")
async def getName(request):
    host = "0.0.0.0:2181,0.0.0.0:2182,0.0.0.0:2183/lujun/zk"
    server_list_str = get_server_list(host)

    if len(server_list_str) >= 2:
        ip_port = server_list_str[1].strip()  # 提取 IP 和端口
        url = f"http://{ip_port}/age"

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}


        try:
            # 发起 HTTP GET 请求
            response_data = requests.get(url=url, params={'param':'1'}, headers={'Connection':'close'})

            if response_data.status_code == 200:
                return response.text(response_data.text)
            else:
                return response.text(f"HTTP request failed with status code: {response_data.status_code}")
        except Exception as e:
            return response.text(f"Error during HTTP request: {str(e)}")
    else:
        return response.text("Server list does not contain enough entries.")


if __name__ == '__main__':
    app.run('localhost', 9999)
