from backend import app
from backend.models import db, User, Demographic, Location, LocationLookup

if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    try:
        db.session.add(User(name="Colin", pwd="gd288288", email="bhchen.2016", phone="90835226"))
        db.session.commit()
    except:
        print("Record exists")
    app.run()
