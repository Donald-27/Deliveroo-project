# backend/app/routes/admin.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from .. import db
from ..models import Parcel, Courier, Incident
from ..utils.assignment import smart_assign_courier
from ..utils.location import reverse_geocode

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/orders", methods=["GET"])
@jwt_required()
def view_orders():
    status = request.args.get("status")
    courier_id = request.args.get("courier_id")
    query = Parcel.query

    if status:
        query = query.filter_by(status=status)
    if courier_id:
        query = query.filter_by(courier_id=courier_id)

    parcels = query.order_by(Parcel.created_at.desc()).all()
    return jsonify([p.to_dict() for p in parcels]), 200

@admin_bp.route("/assign/<parcel_id>", methods=["POST"])
@jwt_required()
def assign_parcel(parcel_id):
    parcel = Parcel.query.get_or_404(parcel_id)
    data = request.get_json()
    courier_id = data.get("courier_id")

    if courier_id == "smart":
        assigned = smart_assign_courier(parcel)
        if not assigned:
            return jsonify({"error": "No courier available"}), 400
    else:
        courier = Courier.query.get_or_404(courier_id)
        parcel.courier_id = courier.id

    parcel.status = "In Transit"
    db.session.commit()
    return jsonify({"msg": "Parcel assigned successfully"}), 200

@admin_bp.route("/update-status/<parcel_id>", methods=["POST"])
@jwt_required()
def update_status(parcel_id):
    parcel = Parcel.query.get_or_404(parcel_id)
    data = request.get_json()
    new_status = data.get("status")
    parcel.status = new_status
    db.session.commit()
    return jsonify({"msg": "Status updated"}), 200

@admin_bp.route("/update-location/<parcel_id>", methods=["POST"])
@jwt_required()
def update_location(parcel_id):
    parcel = Parcel.query.get_or_404(parcel_id)
    data = request.get_json()
    lat, lon = data.get("latitude"), data.get("longitude")
    parcel.current_lat = lat
    parcel.current_lon = lon
    parcel.current_address = reverse_geocode(lat, lon)
    db.session.commit()
    return jsonify({"msg": "Location updated"}), 200

@admin_bp.route("/incidents", methods=["GET"])
@jwt_required()
def view_incidents():
    incidents = Incident.query.order_by(Incident.created_at.desc()).all()
    return jsonify([i.to_dict() for i in incidents]), 200
