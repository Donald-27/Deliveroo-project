# backend/app/routes/parcel_routes.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Parcel, User, db
from datetime import datetime

parcel_bp = Blueprint('parcels', __name__, url_prefix='/api/parcels')

# Create Parcel Delivery Order
@parcel_bp.route('/', methods=['POST'])
@jwt_required()
def create_parcel():
    data = request.get_json()
    user_id = get_jwt_identity()

    try:
        new_parcel = Parcel(
            user_id=user_id,
            pickup_address=data.get('pickup_address'),
            delivery_address=data.get('delivery_address'),
            weight=data.get('weight'),
            instructions=data.get('instructions'),
            status='created',
            current_location=data.get('pickup_address'),
            created_at=datetime.utcnow()
        )
        db.session.add(new_parcel)
        db.session.commit()

        return jsonify({'message': 'Parcel created', 'parcel_id': new_parcel.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# View All Parcels for User
@parcel_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_parcels():
    user_id = get_jwt_identity()
    parcels = Parcel.query.filter_by(user_id=user_id).all()
    return jsonify([p.to_dict() for p in parcels]), 200

# View Specific Parcel by ID
@parcel_bp.route('/<int:parcel_id>', methods=['GET'])
@jwt_required()
def get_parcel(parcel_id):
    user_id = get_jwt_identity()
    parcel = Parcel.query.filter_by(id=parcel_id, user_id=user_id).first()

    if not parcel:
        return jsonify({'error': 'Parcel not found'}), 404
    return jsonify(parcel.to_dict()), 200

# Update Parcel Destination
@parcel_bp.route('/<int:parcel_id>/destination', methods=['PUT'])
@jwt_required()
def update_destination(parcel_id):
    user_id = get_jwt_identity()
    parcel = Parcel.query.filter_by(id=parcel_id, user_id=user_id).first()

    if not parcel:
        return jsonify({'error': 'Parcel not found'}), 404

    if parcel.status == 'delivered':
        return jsonify({'error': 'Cannot change destination after delivery'}), 403

    parcel.delivery_address = request.json.get('new_address')
    db.session.commit()
    return jsonify({'message': 'Destination updated'}), 200

# Cancel Parcel
@parcel_bp.route('/<int:parcel_id>/cancel', methods=['POST'])
@jwt_required()
def cancel_parcel(parcel_id):
    user_id = get_jwt_identity()
    parcel = Parcel.query.filter_by(id=parcel_id, user_id=user_id).first()

    if not parcel:
        return jsonify({'error': 'Parcel not found'}), 404
    if parcel.status == 'delivered':
        return jsonify({'error': 'Cannot cancel delivered parcel'}), 403

    parcel.status = 'cancelled'
    db.session.commit()
    return jsonify({'message': 'Parcel cancelled'}), 200

# Admin Update Parcel Status or Location
@parcel_bp.route('/<int:parcel_id>/admin-update', methods=['PUT'])
@jwt_required()
def admin_update(parcel_id):
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if user.role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.get_json()
    parcel = Parcel.query.get(parcel_id)

    if not parcel:
        return jsonify({'error': 'Parcel not found'}), 404

    parcel.status = data.get('status', parcel.status)
    parcel.current_location = data.get('location', parcel.current_location)
    db.session.commit()

    return jsonify({'message': 'Parcel updated by admin'}), 200
