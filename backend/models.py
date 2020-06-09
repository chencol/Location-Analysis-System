import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import column_property

from backend import app, db_name

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@127.0.0.1:3306/" + db_name
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


class User(db.Model):
    __tablename = "user"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    role = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(11), unique=True)
    purchase_records = db.relationship('PurchaseRecord', backref='user')
    favors = db.relationship('Favor', backref='user')

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "email": self.email,
                "role": self.role
                # "favors": list(
                #     map(lambda favor: favor.serialize(), self.favors))
                }

    def __repr__(self):
        return "User with name " + self.name


class Product(db.Model):
    __tablename = "api"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    total_shares = db.Column(db.Integer)
    shares_avai = db.Column(db.Integer)
    active = db.Column(db.Boolean, default=True, nullable=False)
    purchase_records = db.relationship('PurchaseRecord', backref='product')
    favors = db.relationship('Favor', backref='product')
    pics = db.Column(db.String(100))
    desc = db.Column(db.String(100))
    date_listed = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "category": self.category,
                "total_shares": self.total_shares,
                "shares_avai": self.shares_avai,
                "active": self.active,
                "date_listed": self.date_listed,
                "pics": self.pics,
                "desc": self.desc}


class Favor(db.Model):
    __tablename = "favor"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def serialize(self):
        return {"id": self.id,
                "product": self.product.serialize(),
                "user": self.user.serialize()
                }


class PurchaseRecord(db.Model):
    __tablename = "purchase_record"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    number_of_shares = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_purchase = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    starting_index = db.Column(db.Integer, nullable=False)
    ending_index = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {"id": self.id,
                "number_of_shares": self.number_of_shares,
                "product_id": self.product_id,
                "user_id": self.user_id,
                "date_purchase": self.date_purchase,
                "starting_index": self.starting_index,
                "ending_index": self.ending_index,
                "product": self.product.serialize(),
                "user": self.user.serialize()}


class Demographic(db.Model):
    __tablename = "demographic"
    mac_address = db.Column(db.String(100), primary_key=True, unique=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    gender = db.Column(db.String(1))
    password = db.Column(db.String(100))


class Location(db.Model):
    __tablename = "location"
    location_id = db.Column(db.String(100), db.ForeignKey('location_lookup.location_id'), )
    mac_address = db.Column(db.String(100), primary_key=True)
    timestamp = db.Column(db.DateTime, primary_key=True)


class LocationLookup(db.Model):
    __tablename = "location_lookup"
    location_id = db.Column(db.String(100), primary_key=True, unique=True)
    semantic_place = db.Column(db.String(100))
    locations = db.relationship('Location', backref='location_lookup')
