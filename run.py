from flask import Flask, request, render_template
from app import app, db

application = Flask(__name__)

from app.models import User, Contract, Domain


@application.route("/thanks2buyer")
def thanks1():
    return render_template('thanks2buyer.html')

@application.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return render_template('login.html', username=request.form['username'], callback=request.args.get('callback'))
        else:
            error = 'Invalid username/password.'
    return render_template('login.html', error=error, callback=request.args.get('callback'))

def valid_login(username, password):
    user = User.query.filter_by(username=username).first()

    if user == None:
        return False

    if user.password == password:
        return True
    else:
        return False

@application.route("/add_contract", methods=['GET', 'POST'])
def add_contract():
    if request.method == 'POST':
        domain  = request.form['domain']
        name    = request.form['name']
        email   = request.form['email']

        contract = Contract(domain, name, email)
        db.session.add(contract)
        db.session.commit()

        return render_template('add_contract.html', domain=domain, name=name, email=email)
    else:
        return render_template('add_contract.html')

@application.route("/update_contract", methods=['GET', 'POST'])
def update_contract():
    if request.method == 'POST':
        domain = request.form['domain']
        name = request.form['name']
        email = request.form['email']
        price = request.form['price']

        contract = Contract.query.filter_by(domain = domain).first()

        contract.seller_name  = name
        contract.seller_email = email
        contract.price        = price

        db.session.commit()

        return render_template('update_contract.html', name=name, email=email, price=price)
    else:
        return render_template('update_contract.html')

@application.route("/registrar1")
def registrar1():
    return render_template('registrar1.html')

@application.route("/listDomains")
def listDomains():
    return render_template('listDomains.html', domains=["google.com", "ing.nl", "ing.com", "youtube.com"])

@application.route("/search", methods=['POST'])
def search():
    domains = ["google.com", "ing.nl", "ing.com", "youtube.com"]
    return render_template('listDomains.html', domain=Domain("ing.nl"))

@application.route("/registrar1/token/<token>")
def setToken(token):
    return "want to confirm?"

@application.route("/expense_dashboard/")
def excess():
    return '''  <script type="text/javascript">
                    var token = window.location.href.split("access_token=")[1].split("&state=")[0]; 
                    window.location = "http://localhost:5000/registrar1/token/" + token;
                </script> '''

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)