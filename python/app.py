from flask import Flask, render_template, url_for
import pymysql

app = Flask(__name__)

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    db = 'study_db',
    charset = 'utf8'
)

@app.route("/")  # 기본 홈페이지
def hello_world():
    return render_template('index.html')
#return "<h1>테스트 성공!!</h1>"

@app.route('/test')  # 테스트
def hello():
    curs = conn.cursor()
    sql = "SELECT * FROM customers"
    curs.execute(sql)
    rows = curs.fetchall()
    for row in rows:
        print(row)
    return render_template('test.html', value=rows)

@app.route("/login")  # 로그인 기능
def login():
    return "<h1>작업중입니다.</h1>"

@app.route('/login-enter')
def coupang():
    return render_template('login-enter.html')

if __name__ == "__main__":
    app.run(debug=True)

conn.close()
