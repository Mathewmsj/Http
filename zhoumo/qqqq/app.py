from flask import Flask, render_template
import requests
import schedule
import time
import socket

app = Flask(__name__)

# 替换为你的API密钥
API_KEY = 'YOUR API KEY'  # 请在这里替换为你从 football-data.org 获取的32位API密钥
API_URL = 'https://api.football-data.org/v4/matches'

# 存储分数数据
live_scores = []

def fetch_scores():
    """
    从Football Data API获取当前比赛分数
    """
    global live_scores
    try:
        headers = {'X-Auth-Token': API_KEY}
        response = requests.get(API_URL, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            live_scores = []
            
            if 'matches' in data:
                for match in data['matches']:
                    score_info = {
                        'home_team': match.get('homeTeam', {}).get('name', 'Unknown'),
                        'away_team': match.get('awayTeam', {}).get('name', 'Unknown'),
                        'home_score': match.get('score', {}).get('fullTime', {}).get('home', '-'),
                        'away_score': match.get('score', {}).get('fullTime', {}).get('away', '-'),
                        'status': match.get('status', 'SCHEDULED'),
                        'competition': match.get('competition', {}).get('name', 'Unknown')
                    }
                    live_scores.append(score_info)
            
            print(f"获取到 {len(live_scores)} 场比赛数据")
        else:
            print(f"API调用失败: {response.status_code}")
            live_scores = []
    except Exception as e:
        print(f"获取分数时出错: {str(e)}")
        live_scores = []

# STEP 3: 设置主页路由
@app.route('/')
def load_index_page():
    """
    加载主页
    """
    # STEP 4: 返回主页模板
    return render_template('index.html')

# STEP 5: 设置分数页面路由
@app.route('/scores')
def load_scores_page():
    """
    加载分数页面
    """
    # 获取最新分数
    fetch_scores()
    
    # STEP 6: 返回分数页面模板并传递数据
    return render_template('scores.html', scores=live_scores)

def find_free_port():
    """
    查找一个可用的端口
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        s.listen(1)
        port = s.getsockname()[1]
    return port

if __name__ == '__main__':
    # 初始化时获取一次分数
    fetch_scores()
    
    # 使用默认端口5000
    port = 5000
    print(f"Flask应用运行在 http://127.0.0.1:{port}/")
    print("按 Ctrl+C 停止服务器")
    
    app.run(debug=True, port=port, host='127.0.0.1')

