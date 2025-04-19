from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>테스트 성공!!</p>"

if __name__ == "__main__":
    app.run()