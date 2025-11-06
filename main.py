from myflask import myflask  # 导入自定义的极简框架类
import os

app = myflask("0.0.0.0", 8002)  # 指定监听地址与端口

# 计算项目根目录与 index.html 路径，避免因工作目录不同导致找不到文件
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_HTML_PATH = os.path.join(BASE_DIR, "index.html")

@app.route("/")  # 未指定 methods，默认 GET
def index():
    with open(INDEX_HTML_PATH, "r", encoding="utf-8") as f:
        return f.read()

@app.route("/hello")  # 简单 GET 路由
def hello():
    return "world"

@app.route("/login", methods=["GET"])  # 同一路径不同方法，分别注册
def login():
    return '<form method="post" url="/login"><input name="username" /><input type="submit"/></form>'

@app.route("/login", methods=["POST"])  # POST 提交处理
def login():
    return 'you have submited some thing'

app.run()  # 启动 socket 服务器，进入阻塞循环