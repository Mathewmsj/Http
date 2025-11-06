import os
import sys


# 计算项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 避免同目录下的 http.py 影子遮蔽标准库 http 包（Flask -> Werkzeug 依赖 http.server）
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

from flask import Flask, render_template, send_file

# 使用默认模板目录 templates/ 与静态目录 assets/
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "assets"),
    static_url_path="/assets",
)


# 存储每个人的简历信息
profiles = {
    'self': {
        'name': '张三',
        'age': 28,
        'hobby': '阅读、编程、旅行、摄影',
        'photo': 'avatar.png',
        'brief': '我是一名充满热情的软件工程师，拥有5年的前端开发经验。专注于创建用户友好的Web应用程序，熟练掌握现代前端技术栈。我热爱学习新技术，善于解决复杂问题，具有良好的团队合作精神和沟通能力。在工作中，我注重代码质量和用户体验，致力于通过技术创新为用户创造价值。',
        'experiences': [
            {
                'title': '高级前端工程师 - 北京科技有限公司',
                'date': '2021.06 - 至今',
                'description': '负责公司核心产品的前端开发，参与系统架构设计，带领团队完成多个重要项目。'
            },
            {
                'title': '前端工程师 - 上海互联网公司',
                'date': '2019.03 - 2021.05',
                'description': '参与电商平台的前端开发工作，负责页面交互实现和组件库开发。'
            },
            {
                'title': '初级前端工程师 - 深圳创业公司',
                'date': '2018.07 - 2019.02',
                'description': '负责公司官网和管理后台的前端开发，快速学习并应用新技术。'
            }
        ]
    },
    'a': {
        'name': '李四',
        'age': 26,
        'hobby': '篮球、音乐、编程、健身',
        'photo': 'https://sfile.chatglm.cn/chatglm4/60ec8cb6-d9b4-47c5-9e48-599ddba1cfe1.png',
        'brief': '我是一名积极进取的全栈开发工程师，拥有4年的Web开发经验。擅长前后端技术栈，对系统架构设计有深入理解。我喜欢挑战复杂的技术问题，具有良好的逻辑思维能力和创新意识。在团队中，我乐于分享知识，推动技术进步。',
        'experiences': [
            {
                'title': '全栈工程师 - 杭州科技公司',
                'date': '2020.08 - 至今',
                'description': '负责公司产品的全栈开发，参与技术选型和架构设计，主导微服务改造项目。'
            },
            {
                'title': '后端工程师 - 广州互联网公司',
                'date': '2019.06 - 2020.07',
                'description': '负责API开发和数据库设计，参与系统性能优化工作。'
            },
            {
                'title': '初级开发工程师 - 成都软件公司',
                'date': '2018.03 - 2019.05',
                'description': '参与企业级应用开发，学习并实践敏捷开发流程。'
            }
        ]
    },
    'b': {
        'name': '王五',
        'age': 30,
        'hobby': '绘画、设计、摄影、旅行',
        'photo': 'https://sfile.chatglm.cn/chatglm4/60ec8cb6-d9b4-47c5-9e48-599ddba1cfe1.png',
        'brief': '我是一名富有创意的UI/UX设计师，拥有6年的设计经验。专注于用户体验设计和界面设计，擅长将复杂的业务需求转化为简洁易用的设计方案。我对视觉设计有敏锐的洞察力，注重细节和用户体验的每一个环节。',
        'experiences': [
            {
                'title': '高级UI设计师 - 深圳设计公司',
                'date': '2019.11 - 至今',
                'description': '负责公司核心产品的UI/UX设计，建立设计规范体系，指导设计团队工作。'
            },
            {
                'title': 'UI设计师 - 北京互联网公司',
                'date': '2017.05 - 2019.10',
                'description': '参与移动应用和Web应用的界面设计，负责设计系统建设。'
            },
            {
                'title': '实习设计师 - 上海广告公司',
                'date': '2016.07 - 2017.04',
                'description': '协助完成各类设计项目，学习专业设计流程和工具。'
            }
        ]
    },
    'c': {
        'name': '赵六',
        'age': 27,
        'hobby': '写作、阅读、电影、音乐',
        'photo': 'https://sfile.chatglm.cn/chatglm4/60ec8cb6-d9b4-47c5-9e48-599ddba1cfe1.png',
        'brief': '我是一名专业的产品经理，拥有5年的产品管理经验。擅长用户需求分析和产品规划，具有敏锐的市场洞察力。我注重数据驱动的决策，善于协调跨部门合作，推动产品从概念到落地的全过程。在产品设计中，我始终以用户价值为核心。',
        'experiences': [
            {
                'title': '高级产品经理 - 上海金融科技公司',
                'date': '2020.03 - 至今',
                'description': '负责金融产品的规划和设计，领导产品团队完成多个重要项目上线。'
            },
            {
                'title': '产品经理 - 北京电商平台',
                'date': '2018.06 - 2020.02',
                'description': '负责电商核心功能的产品设计，参与用户增长策略制定。'
            },
            {
                'title': '产品助理 - 深圳创业公司',
                'date': '2017.01 - 2018.05',
                'description': '协助产品经理完成需求文档编写，参与用户调研和数据分析。'
            }
        ]
    }
}


@app.route('/avatar.png')
def serve_avatar():
    avatar_path = os.path.join(BASE_DIR, 'avatar.png')
    if os.path.exists(avatar_path):
        return send_file(avatar_path, mimetype='image/png')
    return ('Avatar not found', 404)


@app.route('/')
def self_cv():
    return render_template("cv.html", profile=profiles['self'])


@app.route('/a')
def a_cv():
    return render_template("cv.html", profile=profiles['a'])


@app.route('/b')
def b_cv():
    return render_template("cv.html", profile=profiles['b'])


@app.route('/c')
def c_cv():
    return render_template("cv.html", profile=profiles['c'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)


