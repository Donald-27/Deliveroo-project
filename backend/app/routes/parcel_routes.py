from flask import Blueprint
from flask_jwt_extended import jwt_required
from ..controllers.parcel_controller import create_parcel, get_user_parcels

parcel_bp = Blueprint('parcels', __name__)

parcel_bp.route('/create', methods=['POST'])(jwt_required()(create_parcel))
parcel_bp.route('/my', methods=['GET'])(jwt_required()(get_user_parcels))
