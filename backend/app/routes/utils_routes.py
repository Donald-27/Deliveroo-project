from flask import Blueprint
from flask_jwt_extended import jwt_required
from ..controllers.utils_controller import generate_qr, geocode_address

utils_bp = Blueprint('utils', __name__)

utils_bp.route('/generate-qr', methods=['POST'])(jwt_required()(generate_qr))
utils_bp.route('/geocode', methods=['POST'])(jwt_required()(geocode_address))
