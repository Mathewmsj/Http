import socket
from typing import Callable, Dict, List, Optional

# 使用标准库 socket 构建一个极简的“类 Flask”框架：
# - 通过 @route 装饰器完成路径与方法的映射
# - 使用内存字典保存路由表
# - 用纯 socket 解析请求行并返回 HTTP 响应


class myflask:
    def __init__(self, host: str = "0.0.0.0", port: int = 8000):
        self.host = host
        self.port = port
        # 设计路由表：按“路径”分组，再按“方法”区分到具体处理函数
        # 这样既能支持同一路径不同方法（如 GET/POST），也便于快速查找
        # 结构：routes[path][method] = handler
        self.routes: Dict[str, Dict[str, Callable[[], str]]] = {}

    def route(self, path: str, methods: Optional[List[str]] = None):
        # 装饰器工厂：允许指定 methods；未指定则默认 GET
        if methods is None or len(methods) == 0:
            methods = ["GET"]
        # 统一转大写，避免大小写不一致导致匹配失败
        methods_upper = [m.upper() for m in methods]

        def decorator(func: Callable[[], str]):
            # 注册：对同一路径为不同方法绑定同一个处理函数
            method_map = self.routes.setdefault(path, {})
            for method in methods_upper:
                method_map[method] = func
            return func

        return decorator

    def run(self):
        # 启动 TCP 服务器：AF_INET + SOCK_STREAM 即 IPv4 的 TCP Socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            # SO_REUSEADDR 便于调试时快速重启，不必等待 TIME_WAIT
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind((self.host, self.port))
            server_socket.listen(5)
            print(f"Server running at {self.host}:{self.port}")

            # 简单的串行 accept/处理循环（教学/作业足够；生产应使用并发/超时等）
            while True:
                conn, addr = server_socket.accept()
                with conn:
                    try:
                        # 读取请求；简单起见一次性读取，不做分块或大包处理
                        request_raw = conn.recv(65536)
                        if not request_raw:
                            continue
                        # 容错解码，避免非法字节导致崩溃
                        request_text = request_raw.decode("utf-8", errors="ignore")
                        # 仅解析请求行：METHOD SP PATH SP VERSION\r\n...
                        first_line = request_text.split("\r\n", 1)[0]
                        parts = first_line.split(" ")
                        if len(parts) < 3:
                            # 请求行不完整 → 400
                            self._send(conn, "400 Bad Request", "Bad Request")
                            continue
                        method, target, _ = parts[0], parts[1], parts[2]
                        # 忽略查询串，仅以“路径部分”做路由匹配
                        path = target.split("?", 1)[0]

                        # 路由分发：优先路径，再匹配方法
                        handler = self._resolve_handler(path, method)
                        if handler is None:
                            # 路径存在但方法不被允许 → 405；否则 → 404
                            if path in self.routes:
                                self._send(conn, "405 Method Not Allowed", "Method Not Allowed")
                            else:
                                self._send(conn, "404 Not Found", "Not Found")
                            continue

                        try:
                            # 执行处理函数；返回值允许 str/bytes，统一转为 bytes 回写
                            result = handler()
                            if isinstance(result, bytes):
                                body_bytes = result
                            else:
                                body_bytes = str(result).encode("utf-8")
                            self._send(conn, "200 OK", body_bytes, is_bytes=True)
                        except Exception:
                            # 业务处理异常 → 500
                            self._send(conn, "500 Internal Server Error", "Internal Server Error")
                    except Exception:
                        # 解析阶段出现异常 → 500（尽量返回可用响应而非直接断开）
                        try:
                            self._send(conn, "500 Internal Server Error", "Internal Server Error")
                        except Exception:
                            pass

    def _resolve_handler(self, path: str, method: str) -> Optional[Callable[[], str]]:
        # 按路径取出方法映射，再以大写方法名查找处理函数
        method_map = self.routes.get(path)
        if not method_map:
            return None
        return method_map.get(method.upper())

    def _send(self, conn: socket.socket, status: str, body: str, is_bytes: bool = False):
        # 统一的响应输出：拼接状态行 + 必要头部 + 实体
        if is_bytes:
            body_bytes = body  # type: ignore[assignment]
        else:
            body_bytes = body.encode("utf-8")
        headers = [
            f"HTTP/1.1 {status}",
            # 简化为 text/html；真实框架会根据返回类型自动协商
            "Content-Type: text/html; charset=utf-8",
            # Content-Length 避免客户端阻塞等待
            f"Content-Length: {len(body_bytes)}",
            # 简化：短连接，响应后直接关闭
            "Connection: close",
            "",
            "",
        ]
        conn.sendall("\r\n".join(headers).encode("utf-8") + body_bytes)


