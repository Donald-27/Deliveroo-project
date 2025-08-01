# backend/app/routes/photo_routes.py

import os
from flask import Blueprint, request, jsonify, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
from app.models import Parcel, User, db

photo_bp = Blueprint('photos', __name__, url_prefix='/api/photos')

UPLOAD_FOLDER = 'backend/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Upload Photo Proof of Delivery
@photo_bp.route('/upload/<int:parcel_id>', methods=['POST'])
@jwt_required()
def upload_proof(parcel_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    parcel = Parcel.query.get(parcel_id)

    if user.role not in ['admin', 'courier']:
        return jsonify({'error': 'Only admin or courier can upload proof'}), 403

    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(f"parcel_{parcel_id}_{file.filename}")
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        parcel.proof_of_delivery = filename
        db.session.commit()

        return jsonify({'message': 'Photo proof uploaded'}), 200

    return jsonify({'error': 'Invalid file type'}), 400

# View Proof of Delivery (if available)
@photo_bp.route('/view/<int:parcel_id>', methods=['GET'])
@jwt_required()
def view_proof(parcel_id):
    user_id = get_jwt_identity()
    parcel = Parcel.query.get(parcel_id)

    if not parcel:
        return jsonify({'error': 'Parcel not found'}), 404

    if not parcel.proof_of_delivery:
        return jsonify({'message': 'No photo proof available'}), 404

    return send_from_directory(UPLOAD_FOLDER, parcel.proof_of_delivery)
