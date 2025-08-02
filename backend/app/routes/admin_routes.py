from flask import Blueprint
from flask_jwt_extended import jwt_required
from ..controllers.admin_controller import get_all_parcels, update_parcel_status

admin_bp = Blueprint('admin', __name__)

admin_bp.route('/all', methods=['GET'])(jwt_required()(get_all_parcels))
admin_bp.route('/update/<int:parcel_id>', methods=['PUT'])(jwt_required()(update_parcel_status))
