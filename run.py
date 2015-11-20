from flask import Flask, request, render_template
from app import app

application = Flask(__name__)


from flask.ext.wtf import Form
from wtforms.fields import TextField, PasswordField
#from wtforms.validators import Required
from app.models import User


class LoginForm(Form):
    username = TextField('Username')
    password = PasswordField('Password')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(
            username=self.username.data).first()
        if user is None:
            self.username.errors.append('Unknown username')
            return False

        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        self.user = user
        return True






@application.route("/")
def hello():
    return render_template('layout.html',variable="This is a variable")

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