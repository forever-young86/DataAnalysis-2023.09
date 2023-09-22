from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')     # localhost:5000/ 을 서비스하기 위한 코드
def index():
    return '<h1>Hello Flask</h1><h2>Flask 좋아요!!!</h2>'

@app.route('/hello')
def hello():
    return render_template('01.hello.html')         # 자동으로 templates 폴더 밑에 있는 파일을 찾음

@app.route('/sub/hello')
def sub_hello():
    return render_template('sub/01.hello.html')     # 똑같이 sub/ 디렉토리 경로도 넣어줘야한다

if __name__ == '__main__':
    app.run(debug=True)     #Debug 모드를 True로 해놓으면 .py파일의 내용이 바뀌면 자동으로 재실행한다.