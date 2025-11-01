"""
Flask 应用 - AJAX 学生列表
功能：提供学生数据 API，前端通过 AJAX 动态加载
"""
from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

# 学生数据（模拟数据库）
students = [
    {
        "id": 1,
        "name": "张三",
        "age": 20,
        "major": "计算机科学",
        "grade": "大二",
        "email": "zhangsan@example.com"
    },
    {
        "id": 2,
        "name": "李四",
        "age": 21,
        "major": "软件工程",
        "grade": "大三",
        "email": "lisi@example.com"
    },
    {
        "id": 3,
        "name": "王五",
        "age": 19,
        "major": "数据科学",
        "grade": "大一",
        "email": "wangwu@example.com"
    },
    {
        "id": 4,
        "name": "赵六",
        "age": 22,
        "major": "人工智能",
        "grade": "大四",
        "email": "zhaoliu@example.com"
    },
    {
        "id": 5,
        "name": "孙七",
        "age": 20,
        "major": "网络安全",
        "grade": "大二",
        "email": "sunqi@example.com"
    }
]


@app.route('/')
def index():
    """主页 - 显示学生列表界面"""
    return render_template('students.html')


@app.route('/students')
def get_students():
    """API 端点 - 返回学生数据（JSON 格式）"""
    return jsonify(students)


if __name__ == '__main__':
    print("=" * 50)
    print("Flask 服务器启动成功！")
    print("访问地址: http://localhost:5000")
    print("学生 API: http://localhost:5000/students")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)

