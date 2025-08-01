# backend/app/routes/auth_routes.py

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.models import User
from app.utils.emailer import send_verification_email, send_password_reset_email
from app import db
import datetime

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already registered'}), 400

    hashed_password = generate_password_hash(data['password'])
    new_user = User(
        name=data['name'],
        email=data['email'],
        password=hashed_password,
        phone=data['phone'],
        address=data['address'],
        is_verified=False
    )
    db.session.add(new_user)
    db.session.commit()

    send_verification_email(data['email'])

    return jsonify({'message': 'Account created. Check your email to verify.'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'error': 'Invalid credentials'}), 401

    if not user.is_verified:
        return jsonify({'error': 'Please verify your email first.'}), 403

    expires = datetime.timedelta(days=2)
    token = create_access_token(identity=user.id, expires_delta=expires)

    return jsonify({'token': token, 'user': user.serialize()}), 200

@auth_bp.route('/verify-email/<email>', methods=['GET'])
def verify_email(email):
    user = User.query.filter_by(email=email).first()
    if user:
        user.is_verified = True
        db.session.commit()
        return jsonify({'message': 'Email verified successfully!'}), 200
    return jsonify({'error': 'Invalid email'}), 404

@auth_bp.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json()
    email = data['email']
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    send_password_reset_email(email)
    return jsonify({'message': 'Reset link sent to your email'}), 200

@auth_bp.route('/edit-profile', methods=['PUT'])
def edit_profile():
    data = request.get_json()
    user = User.query.get(data['user_id'])

    user.name = data['name']
    user.phone = data['phone']
    user.address = data['address']
    db.session.commit()

    return jsonify({'message': 'Profile updated successfully'}), 200
