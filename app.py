from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_workd():
    return "<h1>Hello , World!</h1>"

@app.route("/hello_workd1")
def hello_workd1():
    return "<h1>Hello , World1!</h1>"

@app.route("/hello_workd2")
def hello_workd2():
    return "<h1>Hello , World2!</h1>"

@app.route("/test")
def test():
    a = 6+9
    return "this is my function to run app {0} and {1}".format(a,6)

@app.route("/test2")
def test2():
    data = request.args.get('x')
    print(data)
    return "this is data input from my url {}".format(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    