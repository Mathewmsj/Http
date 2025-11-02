"""
Flask 应用 - AJAX 学生列表
功能：提供学生数据 API，前端通过 AJAX 动态加载
"""
import os
import sys

# 计算项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 避免同目录下的 myhttp.py 影响标准库 http 包（Flask -> Werkzeug 依赖 http.server）
if '' in sys.path:
    try:
        sys.path.remove('')
    except ValueError:
        pass
if BASE_DIR in sys.path:
    try:
        sys.path.remove(BASE_DIR)
    except ValueError:
        pass

from flask import Flask, jsonify, render_template

app = Flask(__name__)

# 学生数据（模拟数据库）- 使用你自己的数据
students = [
    {
        "id": 1,
        "name": "王易宁",
        "age": 17,
        "major": "音乐（乐队）",
        "grade": "高中",
        "email": "wangyining@school.com"
    },
    {
        "id": 2,
        "name": "张翼",
        "age": 17,
        "major": "计算机科学",
        "grade": "高中",
        "email": "zhangyi@school.com"
    },
    {
        "id": 3,
        "name": "灯",
        "age": 17,
        "major": "艺术设计",
        "grade": "高中",
        "email": "deng@school.com"
    },
    {
        "id": 4,
        "name": "木桨",
        "age": 17,
        "major": "体育运动",
        "grade": "高中",
        "email": "mujiang@school.com"
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

