from flask import request, jsonify
from ..models import Parcel
from ..database import db

def get_all_parcels():
    parcels = Parcel.query.all()
    return jsonify([{
        'id': p.id,
        'sender_id': p.sender_id,
        'recipient_name': p.recipient_name,
        'recipient_address': p.recipient_address,
        'weight': p.weight,
        'status': p.status
    } for p in parcels]), 200

def update_parcel_status(parcel_id):
    data = request.get_json()
    status = data.get('status')

    parcel = Parcel.query.get(parcel_id)
    if not parcel:
        return jsonify({'error': 'Parcel not found'}), 404

    parcel.status = status
    db.session.commit()

    return jsonify({'message': 'Status updated'}), 200
