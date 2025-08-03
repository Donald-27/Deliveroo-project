from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from utils.jwt_handler import generate_token
from config import db

def signup():
    data = request.get_json()
    email = data.get('email')
    phone = data.get('phone')
    password = data.get('password')

    if not (email or phone) or not password:
        return jsonify({'error': 'Email or phone and password required'}), 400

    existing_user = User.query.filter(
        (User.email == email) | (User.phone == phone)
    ).first()

    if existing_user:
        return jsonify({'error': 'User already exists'}), 409

    new_user = User(
        email=email,
        phone=phone,
        password=generate_password_hash(password)
    )

    db.session.add(new_user)
    db.session.commit()

    token = generate_token(new_user.id)

    return jsonify({'message': 'Signup successful', 'token': token}), 201

def login():
    data = request.get_json()
    email = data.get('email')
    phone = data.get('phone')
    password = data.get('password')

    if not (email or phone) or not password:
        return jsonify({'error': 'Email or phone and password required'}), 400

    user = User.query.filter(
        (User.email == email) | (User.phone == phone)
    ).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid credentials'}), 401

    token = generate_token(user.id)
    return jsonify({'message': 'Login successful', 'token': token}), 200

def get_profile(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({
        'id': user.id,
        'email': user.email,
        'phone': user.phone,
        'name': user.name,
        'profile_pic': user.profile_pic,
        'total_deliveries': user.total_deliveries,
        'on_time_rate': user.on_time_rate,
        'rating': user.rating,
        'years_experience': user.years_experience,
        'daily_distance': user.daily_distance,
        'availability': user.availability
    }), 200
