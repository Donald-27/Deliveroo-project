from flask import request, jsonify
from ..utils.helpers import generate_qr_code
from ..utils.map_helpers import get_coordinates

def generate_qr():
    data = request.get_json()
    content = data.get('content')
    if not content:
        return jsonify({'error': 'Missing QR content'}), 400

    filename = generate_qr_code(content)
    return jsonify({'qr_code': filename}), 200

def geocode_address():
    data = request.get_json()
    address = data.get('address')
    if not address:
        return jsonify({'error': 'Missing address'}), 400

    coords = get_coordinates(address)
    return jsonify({'coordinates': coords}), 200
