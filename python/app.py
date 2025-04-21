#Flask() : Flask 애플리케이션을 만들어주는 클래스(생성자)
#__name__은 파이썬 내장 변수

#Flask(__name__) : 지금 이 파일을 Flask 앱으로 등록한다 라는 뜻이에요.
#실행 중인 현재 파일의 이름"**을 Flask에게 알려주는 역할을 해요.

from flask import Flask, render_template, request, url_for, redirect
from flaskext.mysql import MySQL #아마 이 부분 오류 뜰 텐데 터미널 창에 pip install Flask-MySQL 입력하면 오류 사라질거임

mysql = MySQL()
app = Flask(__name__)
 
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1004'
app.config['MYSQL_DATABASE_DB'] = 'study_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.secret_key = "ABCDEFG"
mysql.init_app(app)

"""
app = Flask(__name__) #Flask 앱을 하나 만들어서, 여기에 라우팅, 데이터 처리, 렌더링 같은 기능을 추가할 준비를 해놓는 코드입니다.

conn = pymysql.connect(  #pymysql : Python이 MySQL 서버와 통신할 수 있도록 해주는 외부 라이브러리를 불러오는 거예요.
    #conn = pymysql.connect :  여기가 MySQL과 실제로 연결하는 코드입니다! 
    host = 'localhost',  #내 컴퓨터에 설치된 MySQL 서버에 접속 (로컬 개발환경)
    user = 'root',       #DB 로그인할 사용자 계정 (기본은 root)
    password = '1004',   #⚠️ 그 사용자의 비밀번호 
    db = 'study_db',     #사용할 데이터베이스 이름
    charset = 'utf8'     #한글 깨짐 방지용 문자 인코딩 설정
)
"""
                 #/는 루트 경로 (Root URL) 를 뜻함,웹사이트에서 /는 홈페이지, 메인화면 을 의미해요.
@app.route("/") # 메인 페이지
#이건 사용자 브라우저에서 어떤 URL로 접속했을 때 어떤 페이지(함수)가 실행될지를 정하는 부분입니다.
def home(): #사용자가 /에 접속했을 때 실행될 함수 이름입니다. / 이름 마음대로 가능 /💡함수 이름은 중복되면 안 됨
    return render_template('index.html') #Flask가 templates 폴더 안에 있는 index.html 파일을 찾아서,그걸 사용자에게 보여줍니다.
         #render(함수)_template(폴더)("index.html(파일)")"
         #render: Flask에서 HTML 파일을 브라우저에 보여줄 때 쓰는 함수예요. "렌더링하다", 즉 HTML을 브라우저가 볼 수 있게 바꿔주는 것

#@app.route("/")
#@는 데코레이터라고 부르는 문법이고,
#app.route("/")는 Flask에게 알려주는 거예요 : “누군가 웹 브라우저에서 / 주소(= 홈 주소)로 접속하면,아래 있는 함수를 실행시켜줘!”
#즉, http://localhost:5000/ 이 주소로 접속하면 → hello_world() 함수 실행됨!

@app.route('/test')  # 테스트 코드
def test():
    conn = mysql.connect()
    curs = conn.cursor()
    sql = "SELECT * FROM customers"
    curs.execute(sql)
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    conn.close()
    return render_template('test.html', value=rows)

@app.route('/login-enter') # 로그인 페이지
def login_enter():
    return render_template('login-enter.html')

@app.route("/join-membership" , methods=['GET', 'POST']) #회원가입 페이지
def join_membership():
    if request.method == 'POST':
        #https://yong0810.tistory.com/4 참고 자료
        #html파일 속 name값을 가져옴
        name = request.form['name']
        gender = request.form['gender']
        id = request.form['id']
        pw = request.form['pw']

        conn = mysql.connect()
        curs = conn.cursor()
        sql = "INSERT INTO Customers (Username, Gender, LoginID, Password)\
                VALUES ('%s', '%s', '%s', '%s')" % (name, gender, id, pw)
        curs.execute(sql)
        data = curs.fetchall()
        if not data:
            conn.commit()
            curs.close()
            conn.close()
            return "회원가입 성공!"
        else:
            conn.rollback()
            curs.close()
            conn.close()
            return "회원가입 실패"
    return render_template("join-membership.html")

if __name__ == "__main__":  #“지금 이 파일이 직접 실행되고 있는 거라면, 아래 코드를 실행해라.”
    app.run(debug=True)   #조건이 참일 때 실행할 코드임
    #app.run(debug=True) : 이건 Flask 서버를 실행하는 명령이에요.

    # debug=True가 켜져 있으면?
    #1.코드를 수정하면 서버를 자동 재시작
    #2.에러가 나면 브라우저에서 에러 메시지를 보기 좋게 보여줌 (Traceback GUI)

 #__name__ : 파이썬이 모든 .py 파일을 실행할 때 자동으로 만들어주는 내장 변수
#파일마다 __name__이라는 이름이 자동으로 생깁니다
#상황	                                        __name__ 값
#터미널에서 직접 실행할 때 (예: python app.py)	  "__main__"
#다른 파일에서 import 될 때 (예: import app)	    "app"
#
#python app.py : 이렇게 직접 실행했을 때만 아래 코드(app.run(...))를 실행하겠다는 뜻이에요.