import jwt
from datetime import datetime, timedelta
from flask import request, jsonify
from functools import wraps

# SECRET_KEY should ideally come from an environment variable
SECRET_KEY = "your_jwt_secret_key"

def encode_token(payload, exp_minutes=60):
    """
    Encode the payload into a JWT token with an expiry.
    """
    payload["exp"] = datetime.utcnow() + timedelta(minutes=exp_minutes)
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_token(token):
    """
    Decode the JWT token. Returns payload if valid, else None.
    """
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def token_required(f):
    """
    Decorator to protect routes that require authentication.
    Validates JWT from the Authorization header.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]

        if not token:
            return jsonify({"error": "Token is missing"}), 401

        try:
            data = decode_token(token)
            if data is None:
                return jsonify({"error": "Invalid or expired token"}), 401
            request.user = data  # Attach decoded token to request
        except Exception:
            return jsonify({"error": "Token processing failed"}), 401

        return f(*args, **kwargs)
    return decorated
