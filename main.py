import datetime

from backend import app
from backend.models import db, User, Demographic, Location, LocationLookup, Product, PurchaseRecord, Favor

if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    print(str(datetime.datetime.utcnow))
    try:
        db.session.add(User(name="Colin", pwd="gd288288", email="bhchen.2016", phone="90835226", role="admin"))
        db.session.add(
            User(name="Yiwen", pwd="gd288288", email="yiwen.2016", phone="90835227", role="customer"))
        db.session.add(
            Product(name="Ftype", category="car", total_shares=10000, shares_avai=10000, pics="ftype",
                    desc="2020 Jaguar F-Type Coupe"))
        db.session.add(Product(name="Q5", category="car", total_shares=10000, shares_avai=10000, pics="q5",
                               desc="2019 Q5 2.0T Premium 4dr"))
        db.session.add(Favor(product_id=1, user_id=1))
        # db.session.add(
        #     PurchaseRecord(number_of_shares=10, product_id=1, user_id=1, date_purchase=db.func.now()))
        db.session.commit()
    except BaseException as error:
        print('An exception occurred: {}'.format(error))
    app.run()
