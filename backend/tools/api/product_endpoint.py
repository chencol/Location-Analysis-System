from importlib.resources import Resource

from flask import jsonify, abort, request

from backend import app
from backend.models import Product, db


@app.route('/api/products', methods=['GET'])
def get_products():
    # products = Product.query.all()
    # https://www.programiz.com/python-programming/methods/built-in/map
    return jsonify({'products': list(map(lambda product: product.serialize(), Product.query.all()))})


@app.route('/api/product/<int:id>', methods=['GET'])
def get_task(id):
    product = Product.query.filter_by(id=id).first()
    if product:
        return jsonify({"status": 200, "result": {'product': Product.query.get(id).serialize()}})
    else:
        return jsonify({"status": 404, "result": "Not found"})


@app.route('/api/product', methods=['POST'])
def create_product():
    name = request.form.get('name')
    category = request.form.get('category')
    total_shares = request.form.get('total_shares')
    current_shares = request.form.get('current_shares')
    if name and category and total_shares and current_shares:
        db.session.add(
            Product(name=name, category=category, total_shares=int(total_shares), current_shares=int(current_shares)))
        db.session.commit()
        return jsonify(
            {"status": 200,
             "result": {'products': list(map(lambda product: product.serialize(), Product.query.all()))}})
    else:
        return jsonify(
            {"status": 404,
             "result": "Not enough info to create this object"})


@app.route('/api/product/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.filter_by(id=id).first()
    if product:
        name = request.form.get('name')
        category = request.form.get('category')
        total_shares = request.form.get('total_shares')
        current_shares = request.form.get('current_shares')
        if not name and not category and not total_shares and not current_shares:
            return jsonify({"status": 204, "result": "No content"})
        else:
            product.name = name
            product.category = category
            product.total_shares = int(total_shares)
            product.current_shares = int(current_shares)
            db.session.commit()
            return jsonify({"status": 200, "result": product.serialize()})
    else:
        return jsonify({"status": 404, "result": "Not found"})


@app.route('/api/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.filter_by(id=id).first()
    if product:
        db.session.delete(Product.query.get(id))
        db.session.commit()
        return jsonify({"status": 200, "result": "Deleted"})
    else:
        return jsonify({"status": 404, "result": "Not found"})
