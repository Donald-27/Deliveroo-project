from flask import request, jsonify
from models.user import User
from models.parcel import Parcel
from config import db
from werkzeug.security import generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity

@jwt_required()
def get_all_users():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    if not user or user.role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    users = User.query.all()
    output = []
    for u in users:
        output.append({
            'id': u.id,
            'name': u.name,
            'email': u.email,
            'phone': u.phone,
            'role': u.role
        })
    return jsonify({'users': output}), 200

@jwt_required()
def delete_user(user_id):
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    if not user or user.role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    target_user = User.query.get(user_id)
    if not target_user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(target_user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200

@jwt_required()
def get_all_parcels():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    if not user or user.role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    parcels = Parcel.query.all()
    output = []
    for p in parcels:
        output.append({
            'id': p.id,
            'sender': p.sender,
            'recipient': p.recipient,
            'origin': p.origin,
            'destination': p.destination,
            'status': p.status,
            'weight': p.weight,
            'courier_id': p.courier_id,
            'created_at': p.created_at,
            'updated_at': p.updated_at
        })
    return jsonify({'parcels': output}), 200
