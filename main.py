from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def getMethod():
    print('Im in root')
    return render_template('index.html')

@app.route("/hello")
def hellopage():
    print("I'm in hello")
    return render_template('hello.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="8080",debug=True)

