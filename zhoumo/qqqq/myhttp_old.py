import socket

HOST = "0.0.0.0"  # 代表所有 IPv4 地址
PORT = 8082  # 设置端口

class Http:
    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port
        self.conn = None
        self.method = None
        self.path = None
        self.start_server()
    
    def start_server(self):
        """启动HTTP服务器"""
        # 使用 with 语法确保 socket 被自动关闭
        with socket.socket() as s:  # 创建 socket 对象
            s.bind((self.host, self.port))  # 绑定端口（代表接受来自host和port的请求）
            
            s.listen(5)  # 等待客户端连接
            print(f'服务器启动在 {self.host}:{self.port}')
            
            while True:
                conn, addr = s.accept()  # 建立客户端连接
                with conn:
                    print('连接地址：', addr)
                    self.conn = conn
                    request = conn.recv(4096).decode("utf-8", errors="ignore")
                    # 简单解析请求行
                    first_line = request.split("\r\n", 1)[0]
                    method, path, _ = first_line.split(" ", 2)
                    self.method = method
                    self.path = path
                    
                    # 根据路径分发请求
                    if path == "/" or path == "":
                        self.getRoot(path)
                    else:
                        self.get404(path)
    
    def response(self, body, status="200 OK"):
        """发送HTTP响应"""
        resp = (
            f"HTTP/1.1 {status}\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            f"Content-Length: {len(body.encode())}\r\n"
            "Connection: close\r\n\r\n"
            f"{body}"
        )
        self.conn.sendall(resp.encode('utf-8'))  # 发送响应信息
    
    # 以下方法需要在子类中重写
    def getRoot(self, path):
        """处理根路径请求"""
        body = f"<h1>Hello</h1><p>Method={self.method}, Path={path}</p>"
        self.response(body)
    
    def get404(self, path):
        """处理404请求"""
        body = f"<h1>404 Not Found</h1><p>Path={path}</p>"
        self.response(body, status="404 Not Found")

