from flask import Blueprint, request, jsonify, current_app, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from itsdangerous import URLSafeTimedSerializer
from .. import db, mail
from ..models import User, Referral
from flask_mail import Message

auth_bp = Blueprint("auth", __name__)

# Serializer accessor
def get_serializer():
    return URLSafeTimedSerializer(current_app.config["SECRET_KEY"])

def send_email(to, subject, body):
    msg = Message(subject, recipients=[to], body=body)
    mail.send(msg)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    email = data["email"].lower()
    password = data["password"]
    name = data.get("name", "")
    phone = data.get("phone", "")
    referral_code = data.get("referral_code")

    if User.query.filter_by(email=email).first():
        return jsonify({"msg": "Email already registered"}), 400

    # Create user
    user = User(
        email=email,
        password_hash=generate_password_hash(password),
        name=name,
        phone=phone,
        referral_code=User.generate_referral_code()  # implement in model
    )
    db.session.add(user)
    db.session.commit()

    # Handle referral
    if referral_code:
        ref = Referral.query.filter_by(code=referral_code, used=False).first()
        if ref:
            ref.invitee_id = user.id
            ref.used = True
            user.loyalty_points += current_app.config.get("REFERRAL_POINTS", 100)
            ref.inviter.loyalty_points += current_app.config.get("REFERRAL_POINTS", 100)
            db.session.commit()

    # Send email confirmation
    token = get_serializer().dumps(email, salt="email-confirm")
    confirm_url = url_for("auth.confirm_email", token=token, _external=True)
    body = f"Hi {name}, please confirm your email: {confirm_url}"
    send_email(email, "Confirm your Deliveroo account", body)

    return jsonify({"msg": "Registration successful, please confirm your email"}), 201

@auth_bp.route("/confirm/<token>")
def confirm_email(token):
    try:
        email = get_serializer().loads(token, salt="email-confirm", max_age=3600)
    except Exception:
        return jsonify({"msg": "Invalid or expired token"}), 400

    user = User.query.filter_by(email=email).first_or_404()
    user.email_confirmed = True
    db.session.commit()
    return jsonify({"msg": "Email confirmed successfully"}), 200

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data["email"].lower()
    password = data["password"]

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"msg": "Bad credentials"}), 401
    if not getattr(user, "email_confirmed", False):
        return jsonify({"msg": "Email not confirmed"}), 403

    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token}), 200

@auth_bp.route("/forgot-password", methods=["POST"])
def forgot_password():
    email = request.get_json().get("email").lower()
    user = User.query.filter_by(email=email).first_or_404()
    token = get_serializer().dumps(email, salt="password-reset")
    reset_url = url_for("auth.reset_password", token=token, _external=True)
    body = f"Reset your password: {reset_url}"
    send_email(email, "Password Reset for Deliveroo", body)
    return jsonify({"msg": "Password reset email sent"}), 200

@auth_bp.route("/reset-password/<token>", methods=["POST"])
def reset_password(token):
    try:
        email = get_serializer().loads(token, salt="password-reset", max_age=3600)
    except Exception:
        return jsonify({"msg": "Invalid or expired token"}), 400

    data = request.get_json()
    new_password = data.get("password")
    user = User.query.filter_by(email=email).first_or_404()
    user.password_hash = generate_password_hash(new_password)
    db.session.commit()
    return jsonify({"msg": "Password has been reset"}), 200

@auth_bp.route("/profile", methods=["GET", "PUT"])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)

    if request.method == "PUT":
        data = request.get_json()
        user.name = data.get("name", user.name)
        user.phone = data.get("phone", user.phone)
        db.session.commit()

    return jsonify({
        "email": user.email,
        "name": user.name,
        "phone": user.phone,
        "addresses": [addr.to_dict() for addr in user.addresses],
        "templates": [tmpl.to_dict() for tmpl in user.templates],
        "loyalty_points": user.loyalty_points
    }), 200
