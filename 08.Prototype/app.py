from flask import Flask, render_template, request, flash, session
from bp.crawling import crawl_bp
from bp.map import map_bp
from bp.user import user_bp

app = Flask(__name__)
app.secret_key = 'qwert12345'   # flash와 sesstion을 사용하려면 반드시 설정해야 함
app.config['SESSION_COOKIE_PATH'] = '/'

app.register_blueprint(crawl_bp, url_prefix='/crawling')        # localhost:5000/crawling/* 는 crawl_bp가 처리
app.register_blueprint(map_bp, url_prefix='/map')
app.register_blueprint(user_bp, url_prefix='/user')

@app.route('/')
def home():
    menu = {'ho':1, 'us':0, 'cr':0, 'ma':0, 'sc':0}
    # flash('Welcome to my Web!!!')       # alert message가 뜸, base.html에 코드를 넣어놓아야하고, secret_key를 설정해야함
    return render_template('home.html', menu=menu)

@app.route('/schedule')
def schedule():
    menu = {'ho':0, 'us':0, 'cr':0, 'ma':0, 'sc':1}
    return render_template('schedule.html', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)