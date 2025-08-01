# backend/app/routes/referrals.py

from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from .. import db
from ..models import Referral, User
import string, random

referrals_bp = Blueprint("referrals", __name__)

def generate_code(length=8):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@referrals_bp.route("/generate", methods=["POST"])
@jwt_required()
def generate_referral():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)

    # Create a new code or return existing
    existing = Referral.query.filter_by(inviter_id=user_id, used=False).first()
    if existing:
        return jsonify({"code": existing.code}), 200

    code = generate_code()
    ref = Referral(inviter_id=user_id, code=code)
    db.session.add(ref)
    db.session.commit()
    return jsonify({"code": code}), 201

@referrals_bp.route("/apply", methods=["POST"])
@jwt_required()
def apply_referral():
    """
    Apply someone else's code to your account.
    """
    user_id = get_jwt_identity()
    data = request.get_json()
    code = data.get("code")
    ref = Referral.query.filter_by(code=code, used=False).first()
    if not ref:
        return jsonify({"msg": "Invalid or used code"}), 400

    # Mark used and award points
    ref.invitee_id = user_id
    ref.used = True
    inviter = User.query.get(ref.inviter_id)
    invitee = User.query.get(user_id)
    points = current_app.config.get("REFERRAL_POINTS", 100)
    inviter.loyalty_points += points
    invitee.loyalty_points += points

    db.session.commit()
    return jsonify({"msg": f"Referral applied, you earned {points} points"}), 200
