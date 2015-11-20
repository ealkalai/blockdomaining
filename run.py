from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!!</h1>"

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

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)