from flask import Flask, request, render_template
from app import app, db

application = Flask(__name__)

from app.models import User, Contract, Domain

@application.route("/")
def hello():
    return render_template('layout.html',variable="This is a variable")

@application.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return render_template('login.html', username=request.form['username'])
        else:
            error = 'Invalid username/password.'
    return render_template('login.html', error=error)

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

@application.route("/search", methods=['POST'])
def search():
    d1 = Domain("domain1")
    d2 = Domain("domain2")
    d3 = Domain("domain3")

    domains = [d1, d2, d3]
    return render_template('listDomains.html', domains=domains)



if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)