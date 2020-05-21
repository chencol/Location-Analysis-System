from flask import request

from backend import app


@app.route('/demographic')
def demographic():
    return request.method
