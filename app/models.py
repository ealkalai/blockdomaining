from app import db

class User(db.Model):
    __tablename__ = 'users'
    extend_existing=True

    id_u = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(200))
    password = db.Column(db.String(200))


    def __init__(self, username, password):
        self.username   = username
        self.password   = password

    def __repr__(self):
        return "Username: %s" % self.username



class Contract(db.Model):
    __tablename__ = 'contracts'
    extend_existing=True

    id_c            = db.Column(db.Integer, primary_key = True)

    domain          = db.Column(db.String(200))

    buyer_name      = db.Column(db.String(200))
    buyer_email     = db.Column(db.String(200))
    seller_name     = db.Column(db.String(200))
    seller_email    = db.Column(db.String(200))

    price           = db.Column(db.DECIMAL(5,2))

    date_init       = db.Column(db.DateTime)
    date_closure    = db.Column(db.DateTime)
    registrar_email = db.Column(db.String(200))


    def __init__(self, domain):
        self.domain = domain

    def __repr__(self):
        return "Contract ID: %s" % self.id_c


class Domain(db.Model):
    id_d = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String(200))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Domain name: %s" % self.domain


class Registrar(db.Model):
    id_r = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String(200))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Registrar name: %s" % self.domain



