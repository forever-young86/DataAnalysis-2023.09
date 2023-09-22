from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>mehtod 확인</h2><h2>/login으로 확인해 보세요.</h2>'

@app.route('/login', methods=['GET','POST'])        # 사용자 input을 받을때 (Get,Post 메소드를 둘다 받을때)
def login():
    if request.method == 'GET':                     # GET : 화면에서 읽을 form을 보여줌
        return render_template('02.login.html')
    else:                                      # POST: 입력받은 값의 결과를 보여줌
        return '<h1>환영합니다.</h1>'       # 주소창은 똑같이 /login이 뜬다(주소는 변하지 않음!!)

@app.route('/sample', methods=['GET','POST'])
def sample():
    if request.method == 'GET':                
        return render_template('02.sample.html')
    else:                                   
        return '<h1>샘플입니다.</h1>'


if __name__ == '__main__':
    app.run(debug=True)