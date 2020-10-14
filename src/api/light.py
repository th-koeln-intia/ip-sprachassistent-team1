from api.app import app
from api import client
from flask import request, Response


@app.route('/light/<string:friendly_name>/set', methods=['POST'])
def set_light(friendly_name):
    body = request.get_json()
    if body is None:
        return "Bad Request"
    else:
        return body

