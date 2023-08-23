from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def getMethod():
    return render_template('index.html')

@app.route("/hello")
def hellopage():
    return render_template('hello.html')
