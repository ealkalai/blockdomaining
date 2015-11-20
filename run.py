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

@application.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
        	return render_template('loggedIn.html', username=request.form['username'])
        else:
            error = 'Invalid username/password.'
    return render_template('login.html', error=error)

def valid_login(username, password):
	return username == "username" and password == "password"

@application.route("/registrar1")
def registrar1():
    return render_template('registrar1.html')

@application.route("/search", methods=['POST'])
def search():
    domains = ["domain1", "domain2", "domain3"]
    return render_template('listDomains.html', domains=domains)



if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)