from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Float, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class LabelsCreated(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_created = db.Column(db.DateTime(timezone=True), default=func.now())
    label_type = db.Column(db.String(90))
    p_weight = db.Column(db.Float)
    rec_name = db.Column(db.String(150))
    comp_name = db.Column(db.String(150))
    address_1 = db.Column(db.String(250))
    address_2 = db.Column(db.String(250))
    zip_code = db.Column(db.Integer)
    city = db.Column(db.String(250))
    state = db.Column(db.String(250))
    country = db.Column(db.String(250))
    phone = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    currency = db.relationship('Currency')
    labelscreated = db.relationship('LabelsCreated')
