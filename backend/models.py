from flask_sqlalchemy import SQLAlchemy

from backend import app, db_name

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@127.0.0.1:3306/" + db_name
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


class User(db.Model):
    __tablename = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(11), unique=True)

    def __repr__(self):
        return "User with name " + self.name


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
