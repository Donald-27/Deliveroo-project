from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash

from models.user import User
from models.parcel import Parcel
from extensions import db

@jwt_required()
def get_dashboard_stats():
    current_user_id = get_jwt_identity()
    admin_user = User.query.get(current_user_id)

    if not admin_user or admin_user.role != 'admin':
        return jsonify({'error': 'Access denied: Admins only'}), 403

    total_users = User.query.count()
    total_parcels = Parcel.query.count()
    total_couriers = User.query.filter_by(role='courier').count()
    total_customers = User.query.filter_by(role='customer').count()

    parcels_in_transit = Parcel.query.filter_by(status='in_transit').count()
    parcels_delivered = Parcel.query.filter_by(status='delivered').count()
    parcels_pending = Parcel.query.filter_by(status='pending').count()

    return jsonify({
        'users': total_users,
        'parcels': total_parcels,
        'couriers': total_couriers,
        'customers': total_customers,
        'status': {
            'in_transit': parcels_in_transit,
            'delivered': parcels_delivered,
            'pending': parcels_pending
        }
    }), 200


@jwt_required()
def get_all_users():
    current_user_id = get_jwt_identity()
    admin_user = User.query.get(current_user_id)

    if not admin_user or admin_user.role != 'admin':
        return jsonify({'error': 'Access denied: Admins only'}), 403

    users = User.query.all()
    user_list = [
        {
            'id': u.id,
            'name': u.name,
            'email': u.email,
            'phone': u.phone,
            'role': u.role
        }
        for u in users
    ]

    return jsonify({'users': user_list}), 200



@jwt_required()
def toggle_user_access(user_id, data):
    current_user_id = get_jwt_identity()
    admin_user = User.query.get(current_user_id)

    if not admin_user or admin_user.role != 'admin':
        return jsonify({'error': 'Access denied: Admins only'}), 403

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    if 'role' in data:
        user.role = data['role']
    if 'password' in data:
        user.password = generate_password_hash(data['password'])

    db.session.commit()
    return jsonify({'message': 'User updated successfully'}), 200

@jwt_required()
def delete_user(user_id):
    current_user_id = get_jwt_identity()
    admin_user = User.query.get(current_user_id)

    if not admin_user or admin_user.role != 'admin':
        return jsonify({'error': 'Access denied: Admins only'}), 403

    target_user = User.query.get(user_id)

    if not target_user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(target_user)
    db.session.commit()

    return jsonify({'message': f'User {target_user.name} deleted successfully'}), 200


@jwt_required()
def get_all_parcels():
    current_user_id = get_jwt_identity()
    admin_user = User.query.get(current_user_id)

    if not admin_user or admin_user.role != 'admin':
        return jsonify({'error': 'Access denied: Admins only'}), 403

    parcels = Parcel.query.all()
    parcel_list = [
        {
            'id': p.id,
            'sender': p.sender,
            'recipient': p.recipient,
            'origin': p.origin,
            'destination': p.destination,
            'status': p.status,
            'weight': p.weight,
            'courier_id': p.courier_id,
            'created_at': p.created_at.isoformat() if p.created_at else None,
            'updated_at': p.updated_at.isoformat() if p.updated_at else None
        }
        for p in parcels
    ]

    return jsonify({'parcels': parcel_list}), 200
