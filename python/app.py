from flask import Flask, render_template, request, url_for, redirect
import pymysql

app = Flask(__name__)

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    db = 'study_db',
    charset = 'utf8'
)

#conn.close()

@app.route("/")  # 기본 홈페이지
def hello_world():
    return render_template('index.html')

@app.route('/test')  # 테스트
def hello():
    curs = conn.cursor()
    sql = "SELECT * FROM customers"
    curs.execute(sql)
    rows = curs.fetchall()
    for row in rows:
        print(row)
    #curs.close()
    #conn.close()
    return render_template('test.html', value=rows)

@app.route("/login")  # 로그인 기능
def login():
    return "<h1>작업중입니다.</h1>"

@app.route('/login-enter')
def login_enter():
    return render_template('login-enter.html')

@app.route("/join-membership" , methods=['GET', 'POST']) #회원가입 페이지(기능 구현중)
def join():
    if request.method == 'POST':
        #https://yong0810.tistory.com/4 참고 자료
        #html파일 속 name값을 가져옴
        name = request.form['name']
        gender = request.form['gender']
        id = request.form['id']
        pw = request.form['pw']

        curs = conn.cursor()
        sql = "INSERT INTO Customers (Username, Gender, LoginID, Password)\
                VALUES ('%s', '%s', '%s', '%s')" % (name, gender, id, pw)
        curs.execute(sql)
        data = curs.fetchall()
        if not data:
            conn.commit()
            curs.close()
            return "회원가입 성공!"
        else:
            conn.rollback()
            curs.close()
            return "회원가입 실패"
    return render_template("join-membership.html")

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

