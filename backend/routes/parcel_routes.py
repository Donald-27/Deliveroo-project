from flask import Blueprint, request
from controllers.parcel_controller import (
    create_parcel,
    get_all_parcels,
    get_parcel_by_id,
    update_parcel_status,
    get_user_parcels,
    track_parcel
)

parcel_bp = Blueprint('parcel_bp', __name__)

@parcel_bp.route('/book', methods=['POST', 'OPTIONS'])
def create():
    if request.method == 'OPTIONS':
      
        return '', 200
    data = request.json
    return create_parcel(data)

@parcel_bp.route('/', methods=['GET'])
def get_all():
    return get_all_parcels()

@parcel_bp.route('/<int:parcel_id>', methods=['GET'])
def get_by_id(parcel_id):
    return get_parcel_by_id(parcel_id)

@parcel_bp.route('/<int:parcel_id>/status', methods=['PUT'])
def update_status(parcel_id):
    data = request.json
    return update_parcel_status(parcel_id, data)

@parcel_bp.route('/user/<int:user_id>', methods=['GET'])
def get_by_user(user_id):
    return get_user_parcels(user_id)

@parcel_bp.route('/track/<int:parcel_id>', methods=['GET'])
def track(parcel_id):
    return track_parcel(parcel_id)
