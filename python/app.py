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

@app.route("/")
def hello_world():

    curs = conn.cursor()

    # sql = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'customers';"
    sql = "SELECT * FROM customers"

    curs.execute(sql)

    rows = curs.fetchall()
    for row in rows:
        print(row)

    return "<h1>테스트 성공!!</h1>"

@app.route('/test')
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

conn.close()