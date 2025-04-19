from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>테스트 성공!!</h1>"

@app.route('/test')
def hello():
    return render_template('index.html')

@app.route('/king')
def king():
    return render_template('king.html')

if __name__ == "__main__":
    app.run(debug=True)