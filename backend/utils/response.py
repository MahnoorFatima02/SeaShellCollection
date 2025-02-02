from flask import jsonify

def create_response(data=None, status_code=200):
    if data is None:
        data = {}
    elif hasattr(data, 'to_dict'):
        data = data.to_dict()
    return jsonify(data), status_code