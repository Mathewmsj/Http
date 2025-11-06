# Flask 足球比分查询应用

这是一个使用 Flask 框架开发的足球比分查询 Web 应用，通过 Football Data API 获取实时足球比赛数据。

## 🎯 项目特点

- ✨ 使用 Flask 的静态文件处理系统
- 📁 清晰的项目结构（templates 和 static 文件夹分离）
- 🎨 现代化的响应式界面设计
- ⚽ 实时获取足球比赛分数
- 🖼️ SVG 图标和自定义样式

## 📁 项目结构

```
qqqq/
├── app.py                      # Flask 应用主程序
├── templates/                  # HTML 模板文件夹
│   ├── index.html             # 主页模板
│   └── scores.html            # 分数页面模板
├── static/                    # 静态文件夹
│   ├── css/                   # CSS 样式文件
│   │   ├── style.css         # 通用样式
│   │   ├── index.css         # 主页样式
│   │   └── scores.css        # 分数页面样式
│   └── images/               # 图片资源
│       ├── soccer-ball.svg   # 足球图标
│       ├── soccer-ball.png   # 足球PNG图标
│       ├── trophy.svg        # 奖杯图标
│       └── no-data.svg       # 无数据图标
├── requirements.txt          # Python 依赖包
├── .gitignore               # Git 忽略文件配置
└── README.md                # 项目说明文档
```

## 🚀 安装步骤

### 1. 克隆项目

```bash
git clone <你的仓库URL>
cd qqqq
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

或者手动安装：

```bash
pip install Flask requests schedule
```

### 3. 获取 API 密钥

1. 访问 [Football Data API](https://www.football-data.org/)
2. 注册一个免费账户
3. 获取你的 32 位 API 密钥

### 4. 配置 API 密钥

打开 `app.py` 文件，找到第 9 行：

```python
API_KEY = 'YOUR API KEY'
```

将 `YOUR API KEY` 替换为你从 Football Data API 获取的实际 API 密钥。

## 💻 运行应用

1. 在终端中导航到项目文件夹：
   ```bash
   cd /path/to/qqqq
   ```

2. 运行应用：
   ```bash
   python app.py
   ```

3. 打开浏览器，访问：
   ```
   http://127.0.0.1:5000/
   ```

## 📖 使用说明

### 主页 (`/`)
- 显示欢迎信息
- 点击 "View scores!" 按钮查看比赛分数

### 分数页面 (`/scores`)
- 显示当前的足球比赛分数列表
- 包含比赛状态（未开始、直播中、已结束）
- 可以点击刷新按钮更新数据

## 🛠️ 技术栈

- **后端**: Flask (Python)
- **API**: Football Data API
- **前端**: HTML5 + CSS3
- **HTTP 客户端**: requests 库
- **静态文件处理**: Flask 内置 `url_for()` 函数

## 📝 Flask 静态文件处理

本项目使用 Flask 的内置静态文件处理功能：

### 在 HTML 中引用静态文件

```html
<!-- CSS 文件 -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">

<!-- 图片文件 -->
<img src="{{ url_for('static', filename='images/soccer-ball.png') }}" alt="Soccer Ball">
```

### 文件组织

- 所有 CSS 文件放在 `/static/css/` 目录
- 所有图片文件放在 `/static/images/` 目录
- Flask 会自动处理这些静态资源的路由

## ⚠️ 注意事项

- 免费 API 账户每天有 10 次请求限制
- 确保网络连接正常以获取数据
- API 密钥需要保密，不要提交到 Git 仓库
- 建议使用环境变量来存储 API 密钥

## 📚 学习要点

这个项目涵盖了以下 Flask 概念：

1. **路由装饰器**: `@app.route('/')`
2. **模板渲染**: `render_template()`
3. **静态文件处理**: `url_for('static', filename='...')`
4. **Jinja2 模板引擎**: 使用 `{{ }}` 和 `{% %}` 语法
5. **API 集成**: 使用 `requests` 库调用外部 API
6. **项目结构**: templates 和 static 文件夹的组织

## 📄 许可证

本项目仅用于学习目的（Coursera Flask 课程练习）。

## 👨‍💻 开发者

课程练习项目

---

**Happy Coding! ⚽🎉**

