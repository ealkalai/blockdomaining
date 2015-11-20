from flask import Flask, request, render_template
application = Flask(__name__)

@application.route("/")
def hello():
    return render_template('layout.html',variable="This is a variable")

@application.route("/antigoni")
def antigoni():
    return "Hello Antigoni"

@application.route("/robin")
def robin():
    return "Hello Robin"

@application.route("/jens")
def jens():
    return "Hello Jens"

@application.route("/erikos")
def erikos():
    return "Hello Erikos"

@application.route("/maryna")
def maryna():
    return "Hello Maryna"

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)