from flask import Blueprint, request
from controllers.parcel_controller import (
    create_parcel,
    get_all_parcels,
    get_parcel_by_id,
    update_parcel_status,
    get_user_parcels
)

parcel_bp = Blueprint('parcel', __name__)

@parcel_bp.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    return create_parcel(data)

@parcel_bp.route('/', methods=['GET'])
def all_parcels():
    return get_all_parcels()

@parcel_bp.route('/<int:parcel_id>', methods=['GET'])
def parcel_by_id(parcel_id):
    return get_parcel_by_id(parcel_id)

@parcel_bp.route('/<int:parcel_id>/status', methods=['PUT'])
def update_status(parcel_id):
    data = request.get_json()
    return update_parcel_status(parcel_id, data)

@parcel_bp.route('/user/<int:user_id>', methods=['GET'])
def user_parcels(user_id):
    return get_user_parcels(user_id)
