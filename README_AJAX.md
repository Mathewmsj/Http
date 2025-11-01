# AJAX 学生列表项目

## 项目简介

这是一个使用 Flask + AJAX 实现的学生管理系统演示项目。展示了如何：
- 使用 Flask 创建 RESTful API
- 前端通过 AJAX 动态加载数据
- JavaScript 动态创建 DOM 元素
- 前后端分离的开发模式

## 功能特点

✅ **后端 API**
- Flask 框架搭建
- `/students` 端点返回 JSON 数据
- 模拟数据库存储学生信息

✅ **前端动态加载**
- 使用 Fetch API 发送 AJAX 请求
- 纯 JavaScript 动态创建 DOM
- 美观的卡片式布局
- 加载动画和错误处理

✅ **数据展示**
- 学生基本信息展示
- 统计信息自动计算
- 响应式设计

## 项目结构

```
.
├── app.py                      # Flask 主应用
├── templates/
│   └── students.html          # 前端页面（AJAX 实现）
├── requirements.txt           # Python 依赖
└── README_AJAX.md            # 项目说明
```

## 安装运行

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行服务器

```bash
python app.py
```

### 3. 访问应用

打开浏览器访问：
- 主页：http://localhost:5000
- API：http://localhost:5000/students

## 技术实现

### 后端（Flask）

```python
@app.route('/students')
def get_students():
    """返回学生数据（JSON 格式）"""
    return jsonify(students)
```

### 前端（JavaScript + AJAX）

```javascript
// 使用 Fetch API 加载数据
fetch('/students')
    .then(response => response.json())
    .then(data => {
        // 动态创建 DOM 元素
        renderStudents(data);
    });
```

## API 文档

### GET /students

返回所有学生数据

**响应示例：**
```json
[
    {
        "id": 1,
        "name": "张三",
        "age": 20,
        "major": "计算机科学",
        "grade": "大二",
        "email": "zhangsan@example.com"
    }
]
```

## 关键代码说明

### 1. AJAX 请求

使用现代的 `fetch` API 替代传统的 XMLHttpRequest：

```javascript
fetch('/students')
    .then(response => response.json())
    .then(data => renderStudents(data))
    .catch(error => console.error('Error:', error));
```

### 2. 动态创建 DOM

使用 JavaScript 动态创建元素，而不是在 HTML 中硬编码：

```javascript
function createStudentCard(student) {
    const card = document.createElement('div');
    card.className = 'student-card';
    card.innerHTML = `...`;
    return card;
}
```

### 3. JSON 数据交互

后端返回 JSON 格式数据，前端解析并使用：

```python
# 后端
return jsonify(students)

# 前端
.then(data => console.log(data))
```

## 学习要点

1. **前后端分离**：HTML 中不包含数据，所有数据通过 API 获取
2. **异步加载**：使用 AJAX 实现无刷新加载数据
3. **DOM 操作**：JavaScript 动态创建和插入 HTML 元素
4. **RESTful API**：规范的 API 设计
5. **错误处理**：处理网络请求失败的情况

## 扩展功能建议

- [ ] 添加学生（POST 请求）
- [ ] 删除学生（DELETE 请求）
- [ ] 编辑学生信息（PUT 请求）
- [ ] 搜索和筛选功能
- [ ] 分页加载
- [ ] 连接真实数据库

## 常见问题

**Q: 为什么要使用 AJAX？**
A: AJAX 允许网页在不重新加载的情况下更新数据，提供更好的用户体验。

**Q: Fetch API 和 XMLHttpRequest 的区别？**
A: Fetch 是更现代的 API，基于 Promise，语法更简洁。

**Q: 为什么不直接在 HTML 中写数据？**
A: 前后端分离是现代 Web 开发的标准做法，便于维护和扩展。

## 作者

学生作业项目 - 2025

## 许可证

MIT License

