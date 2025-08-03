from flask import request, jsonify
from models.parcel import Parcel
from config import db
from utils.smart_assign import assign_courier
from flask_jwt_extended import get_jwt_identity

def create_parcel():
    data = request.get_json()
    sender = data.get('sender')
    recipient = data.get('recipient')
    origin = data.get('origin')
    destination = data.get('destination')
    weight = data.get('weight')

    if not all([sender, recipient, origin, destination, weight]):
        return jsonify({'error': 'All fields are required'}), 400

    courier_id = assign_courier(origin, destination)

    new_parcel = Parcel(
        sender=sender,
        recipient=recipient,
        origin=origin,
        destination=destination,
        weight=weight,
        courier_id=courier_id
    )

    db.session.add(new_parcel)
    db.session.commit()

    return jsonify({'message': 'Parcel created successfully', 'parcel_id': new_parcel.id}), 201

def track_parcel(parcel_id):
    parcel = Parcel.query.get(parcel_id)
    if not parcel:
        return jsonify({'error': 'Parcel not found'}), 404

    return jsonify({
        'id': parcel.id,
        'sender': parcel.sender,
        'recipient': parcel.recipient,
        'origin': parcel.origin,
        'destination': parcel.destination,
        'weight': parcel.weight,
        'status': parcel.status,
        'courier_id': parcel.courier_id,
        'created_at': parcel.created_at,
        'updated_at': parcel.updated_at
    }), 200

def update_status(parcel_id):
    data = request.get_json()
    status = data.get('status')

    if not status:
        return jsonify({'error': 'Status is required'}), 400

    parcel = Parcel.query.get(parcel_id)
    if not parcel:
        return jsonify({'error': 'Parcel not found'}), 404

    parcel.status = status
    db.session.commit()

    return jsonify({'message': 'Parcel status updated successfully'}), 200
