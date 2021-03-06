from importlib.resources import Resource

from flask import jsonify, abort, request
from sqlalchemy import desc

from backend import app
from backend.models import PurchaseRecord, db, PurchaseRecord, Product, User


@app.route("/api/purchase_records", methods=["GET"])
def get_purchase_records():
    # https://www.programiz.com/python-programming/methods/built-in/map
    return jsonify(
        {
            "purchase_records": list(
                map(
                    lambda purchase_record: purchase_record.serialize(),
                    PurchaseRecord.query.all(),
                )
            )
        }
    )


@app.route("/api/purchase_record/<int:id>", methods=["GET"])
def get_purchase_record(id):
    purchase_record = PurchaseRecord.query.filter_by(id=id).first()
    if purchase_record:
        return jsonify(
            {
                "status": 200,
                "result": {"purchase_record": PurchaseRecord.query.get(id).serialize()},
            }
        )
    else:
        return jsonify({"status": 404, "result": "Not found"})


@app.route("/api/purchase_record", methods=["POST"])
def create_purchase_record():
    product_id = request.form.get("product_id")
    number_of_shares = request.form.get("number_of_shares")
    user_id = request.form.get("user_id")
    if product_id and user_id and number_of_shares:
        starting_index = None
        ending_index = None
        product = Product.query.filter_by(id=int(product_id)).first()
        user = User.query.filter_by(id=int(user_id)).first()
        if product and user:
            if product.active:
                record = (
                    PurchaseRecord.query.order_by(desc(PurchaseRecord.date_purchase))
                    .filter_by(user_id=int(user_id), product_id=int(product_id))
                    .first()
                )
                if product.shares_avai < int(number_of_shares):
                    return jsonify({"status": 404, "result": "Not enough shares!"})
                else:
                    if record:
                        ending_index = record.ending_index
                        starting_index = ending_index + 1
                        ending_index = starting_index + int(number_of_shares) - 1
                    else:
                        starting_index = 1
                        ending_index = starting_index + int(number_of_shares) - 1
                db.session.add(
                    PurchaseRecord(
                        number_of_shares=number_of_shares,
                        user_id=int(user_id),
                        product_id=int(product_id),
                        starting_index=starting_index,
                        ending_index=ending_index,
                    )
                )
                product.shares_avai = product.shares_avai - int(number_of_shares)
                db.session.commit()
            return jsonify({"status": 200, "result": "Purchase successfully"})
        else:
            return jsonify({"status": 404, "result": "Product not available"})
    else:
        return jsonify({"status": 404, "result": "Not found"})


#     db.session.add(PurchaseRecord(number_of_shares=number_of_shares, ))
#     db.session.commit()
#     return jsonify(
#         {"status": 200,
#          "result": {'purchase_records': list(
#              map(lambda purchase_record: purchase_record.serialize(), PurchaseRecord.query.all()))}})
# else:
#     return jsonify(
#         {"status": 404,
#          "result": "Not enough info to create this object"})


@app.route("/api/purchase_record/<int:id>", methods=["PUT"])
def update_purchase_record(id):
    return jsonify({"status": 405, "result": "Method Not Allowed"})


@app.route("/api/api/<int:id>", methods=["DELETE"])
def delete_purchase_record(id):
    purchase_record = PurchaseRecord.query.filter_by(id=id).first()
    if purchase_record:
        db.session.delete(PurchaseRecord.query.get(id))
        db.session.commit()
        return jsonify({"status": 200, "result": "Deleted"})
    else:
        return jsonify({"status": 404, "result": "Not found"})
