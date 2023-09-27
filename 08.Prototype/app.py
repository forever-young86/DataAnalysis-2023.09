from flask import Flask, render_template, request, flash, session
from bp.crawling import crawl_bp
from bp.map import map_bp
from bp.user import user_bp
import os, random
import util.map_util as mu
import util.weather_util as wu


app = Flask(__name__)
app.secret_key = 'qwert12345'   # flash와 sesstion을 사용하려면 반드시 설정해야 함
app.config['SESSION_COOKIE_PATH'] = '/'

app.register_blueprint(crawl_bp, url_prefix='/crawling')        # localhost:5000/crawling/* 는 crawl_bp가 처리
app.register_blueprint(map_bp, url_prefix='/map')
app.register_blueprint(user_bp, url_prefix='/user')

@app.before_first_request   # 최초 한번만 실행
def before_first_request():
    global quotes    # global 변수를 쓰면 다른쪽에서도 수정가능하다
    filename = os.path.join(app.static_folder, 'data/todayQuote.txt')
    with open(filename, encoding='utf-8') as file:
        quotes = file.readlines()   # 리스트 형태로 읽는다
    session['quote'] = random.sample(quotes, 1)[0]     # 1개를 불러오는데, 리스트형이므로 인덱스로 불러온다
    session['addr'] = '서울시 영등포구'

# for AJAX ###############################################
@app.route('/change_quote')
def change_quote():
    quote = random.sample(quotes, 1)[0]
    session['quote'] = quote
    return quote

@app.route('/change_addr')
def change_addr():
    addr = request.args.get('addr')
    session['addr'] = addr
    return addr

@app.route('/weather')
def weather():
    # 서울시 영등포구 + '청' - 도로명 주소 -> 카카오 로컬 -> 좌표 획득 
    addr = request.args.get('addr')     
    lat, lng = mu.get_coord(app.static_folder, addr + '청')
    html = wu.get_weather(app.static_folder, lat, lng)
    return html

 ###############################################

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