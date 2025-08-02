from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from ..models import Parcel
from ..database import db
from ..utils.helpers import generate_qr_code

def create_parcel():
    user = get_jwt_identity()
    data = request.get_json()

    parcel = Parcel(
        sender_id=user['id'],
        recipient_name=data['recipient_name'],
        recipient_address=data['recipient_address'],
        weight=data['weight']
    )
    db.session.add(parcel)
    db.session.commit()

    return jsonify({'message': 'Parcel created successfully', 'parcel_id': parcel.id}), 201

def get_user_parcels():
    user = get_jwt_identity()
    parcels = Parcel.query.filter_by(sender_id=user['id']).all()
    return jsonify([{
        'id': p.id,
        'recipient_name': p.recipient_name,
        'recipient_address': p.recipient_address,
        'weight': p.weight,
        'status': p.status
    } for p in parcels]), 200
