# 使用官方的Python 3.9镜像作为基础镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器中
COPY ./advanced/sanic_blueprint.py /app/

# 安装Sanic和依赖
RUN pip install sanic

# 暴露应用程序的端口（根据需要修改）
EXPOSE 8000

# 定义启动命令
CMD ["python", "sanic_blueprint.py"]
