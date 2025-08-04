from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from utils.jwt_handler import generate_token
from extensions import db


def register_user(data):
    email = data.get('email')
    phone = data.get('phone')
    password = data.get('password')
    full_name = data.get('full_name')

    if not (email or phone) or not password or not full_name:
        return jsonify({'error': 'Full name, email or phone, and password are required'}), 400

    existing_user = User.query.filter(
        (User.email == email) | (User.phone == phone)
    ).first()

    if existing_user:
        return jsonify({'error': 'User already exists'}), 409

    new_user = User(
        email=email,
        phone=phone,
        full_name=full_name
    )
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    token = generate_token(new_user.id)

    return jsonify({'message': 'Signup successful', 'token': token}), 201


def login_user(data):
    email = data.get('email')
    phone = data.get('phone')
    password = data.get('password')

    if not (email or phone) or not password:
        return jsonify({'error': 'Email or phone and password required'}), 400

    user = User.query.filter(
        (User.email == email) | (User.phone == phone)
    ).first()

    if not user or not user.check_password(password):
        return jsonify({'error': 'Invalid credentials'}), 401

    token = generate_token(user.id)
    return jsonify({'message': 'Login successful', 'token': token}), 200


def get_profile(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify(user.to_dict()), 200
