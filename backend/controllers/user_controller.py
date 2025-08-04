from flask import request, jsonify
from models.user import User, db
from utils.jwt_handler import decode_token
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]  

        if not token:
            return jsonify({"message": "Token is missing!"}), 401

        try:
            user_data = decode_token(token)
            current_user = User.query.get(user_data["user_id"])
        except:
            return jsonify({"message": "Token is invalid!"}), 401

        return f(current_user, *args, **kwargs)
    return decorated


def get_all_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200


def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify(user.to_dict()), 200


@token_required
def update_user(current_user, user_id):
    if str(current_user.id) != str(user_id) and current_user.role != "admin":
        return jsonify({"message": "Unauthorized"}), 403

    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    data = request.json
    user.full_name = data.get("full_name", user.full_name)
    user.email = data.get("email", user.email)
    user.phone = data.get("phone", user.phone)
    user.profile_pic = data.get("profile_pic", user.profile_pic)

    db.session.commit()
    return jsonify(user.to_dict()), 200


@token_required
def delete_user(current_user, user_id):
    if current_user.role != "admin":
        return jsonify({"message": "Unauthorized"}), 403

    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200
