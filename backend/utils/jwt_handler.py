import jwt
from datetime import datetime, timedelta
from flask import request, jsonify
from functools import wraps
import os

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_jwt_secret_key")

def generate_token(user_id, role=None, exp_minutes=60):
    """
    Generate a JWT token with user ID and optional role.
    """
    payload = {
        "sub": user_id,
        "role": role,
        "exp": datetime.utcnow() + timedelta(minutes=exp_minutes)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_token(token):
    """
    Decode the JWT token and return the payload if valid.
    """
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def token_required(f):
    """
    Decorator to protect routes with JWT authentication.
    Attaches `request.user` containing decoded payload.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        token = auth_header.split(" ")[1] if auth_header.startswith("Bearer ") else None

        if not token:
            return jsonify({"error": "Token is missing"}), 401

        payload = decode_token(token)
        if not payload:
            return jsonify({"error": "Invalid or expired token"}), 401

        request.user = payload
        return f(*args, **kwargs)
    return decorated

def role_required(allowed_roles):
    """
    Optional decorator to restrict access by user role.
    Usage: @role_required(["admin", "courier"])
    """
    def wrapper(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            user = getattr(request, "user", None)
            if not user or user.get("role") not in allowed_roles:
                return jsonify({"error": "Unauthorized role"}), 403
            return f(*args, **kwargs)
        return decorated
    return wrapper
