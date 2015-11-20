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

    id_c = db.Column(db.Integer, primary_key = True)
    domain = db.Column(db.String(200))

    def __init__(self, domain):
        self.domain = domain

    def __repr__(self):
        return "Domain in contract: %s" % self.domain