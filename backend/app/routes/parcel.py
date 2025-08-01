# backend/app/routes/parcel.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from .. import db
from ..models import Parcel, Address, Template, TimelineEvent
from ..services.delivery_service import calculate_price

parcel_bp = Blueprint("parcel", __name__)

def add_timeline_event(parcel, status, note=""):
    event = TimelineEvent(parcel_id=parcel.id, status=status, note=note)
    db.session.add(event)
    db.session.commit()

@parcel_bp.route("/", methods=["GET"])
@jwt_required()
def list_parcels():
    user_id = get_jwt_identity()
    parcels = Parcel.query.filter_by(user_id=user_id).order_by(Parcel.created_at.desc()).all()
    return jsonify([p.to_dict() for p in parcels]), 200

@parcel_bp.route("/", methods=["POST"])
@jwt_required()
def create_parcel():
    """
    Supports:
      - single parcel (no bulk_id)
      - bulk booking if `bulk_id` provided or multiple items in payload
    """
    user_id = get_jwt_identity()
    data = request.get_json()

    bulk_id = data.get("bulk_id")  # optional grouping ID
    items = data.get("items")      # list of parcel details for bulk
    template_id = data.get("template_id")
    scheduled_at = data.get("scheduled_at")
    eco_mode = data.get("eco_mode", False)

    created = []
    # If template is provided, override fields
    template_data = {}
    if template_id:
        tmpl = Template.query.get_or_404(template_id)
        template_data = tmpl.data

    def make_parcel(item):
        origin = Address.query.get(item.get("origin_id"))
        dest = Address.query.get(item.get("destination_id"))
        p = Parcel(
            user_id=user_id,
            bulk_id=bulk_id,
            origin_id=origin.id,
            destination_id=dest.id,
            weight_kg=item.get("weight_kg", template_data.get("weight_kg")),
            eco_mode=eco_mode,
            scheduled_at=datetime.fromisoformat(scheduled_at) if scheduled_at else None
        )
        db.session.add(p)
        db.session.flush()
        price = calculate_price(p.weight_kg, origin, dest, eco_mode)
        p.base_price = price
        db.session.commit()
        add_timeline_event(p, "created", "Parcel order created")
        created.append(p)
        return p

    if items:
        # Bulk booking
        if not bulk_id:
            bulk_id = f"bulk-{datetime.utcnow().timestamp()}"
        for item in items:
            make_parcel(item)
    else:
        # Single parcel fields
        make_parcel(data)

    return jsonify([p.to_dict() for p in created]), 201

@parcel_bp.route("/<parcel_id>", methods=["GET"])
@jwt_required()
def get_parcel(parcel_id):
    user_id = get_jwt_identity()
    p = Parcel.query.filter_by(id=parcel_id, user_id=user_id).first_or_404()
    return jsonify(p.to_full_dict()), 200

@parcel_bp.route("/<parcel_id>", methods=["PUT"])
@jwt_required()
def edit_parcel(parcel_id):
    """
    Allows destination change before delivery.
    """
    user_id = get_jwt_identity()
    data = request.get_json()
    p = Parcel.query.filter_by(id=parcel_id, user_id=user_id).first_or_404()
    if p.status == "delivered":
        return jsonify({"msg": "Cannot modify delivered parcel"}), 400

    dest_id = data.get("destination_id")
    if dest_id:
        p.destination_id = dest_id
        db.session.commit()
        add_timeline_event(p, "destination_changed", "Destination updated by user")

    return jsonify(p.to_dict()), 200

@parcel_bp.route("/<parcel_id>", methods=["DELETE"])
@jwt_required()
def cancel_parcel(parcel_id):
    """
    Cancel if not yet delivered.
    """
    user_id = get_jwt_identity()
    p = Parcel.query.filter_by(id=parcel_id, user_id=user_id).first_or_404()
    if p.status == "delivered":
        return jsonify({"msg": "Cannot cancel delivered parcel"}), 400

    p.status = "cancelled"
    db.session.commit()
    add_timeline_event(p, "cancelled", "Parcel order cancelled by user")
    return jsonify({"msg": "Parcel cancelled"}), 200
