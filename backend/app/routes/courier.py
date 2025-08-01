# backend/app/routes/courier.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
import os
from .. import db
from ..models import Parcel, Incident, Performance, Courier
from ..utils.location import reverse_geocode
from ..utils.photo import save_proof_photo

courier_bp = Blueprint("courier", __name__)

@courier_bp.route("/deliveries", methods=["GET"])
@jwt_required()
def get_assigned_deliveries():
    courier_id = get_jwt_identity()
    parcels = Parcel.query.filter_by(courier_id=courier_id, status="In Transit").all()
    return jsonify([p.to_dict() for p in parcels]), 200

@courier_bp.route("/deliveries/<parcel_id>/complete", methods=["POST"])
@jwt_required()
def complete_delivery(parcel_id):
    parcel = Parcel.query.get_or_404(parcel_id)
    courier_id = get_jwt_identity()

    if parcel.courier_id != courier_id:
        return jsonify({"error": "Unauthorized"}), 403

    if "photo" not in request.files:
        return jsonify({"error": "Proof photo required"}), 400

    photo = request.files["photo"]
    filename = save_proof_photo(photo, parcel_id)

    parcel.status = "Delivered"
    parcel.photo_proof = filename
    db.session.commit()

    return jsonify({"msg": "Delivery completed", "photo": filename}), 200

@courier_bp.route("/incident", methods=["POST"])
@jwt_required()
def report_incident():
    data = request.get_json()
    courier_id = get_jwt_identity()
    parcel_id = data.get("parcel_id")
    description = data.get("description")

    report = Incident(parcel_id=parcel_id, courier_id=courier_id, description=description)
    db.session.add(report)
    db.session.commit()
    return jsonify({"msg": "Incident reported"}), 201

@courier_bp.route("/performance", methods=["POST"])
@jwt_required()
def log_performance():
    data = request.get_json()
    courier_id = get_jwt_identity()

    record = Performance(
        courier_id=courier_id,
        successful_deliveries=data.get("successful_deliveries"),
        failed_deliveries=data.get("failed_deliveries"),
        delivery_time_avg=data.get("delivery_time_avg"),
        distance_covered_km=data.get("distance_covered_km"),
    )
    db.session.add(record)
    db.session.commit()
    return jsonify({"msg": "Performance logged"}), 201

@courier_bp.route("/update-location/<parcel_id>", methods=["POST"])
@jwt_required()
def update_location(parcel_id):
    data = request.get_json()
    lat = data.get("latitude")
    lon = data.get("longitude")
    parcel = Parcel.query.get_or_404(parcel_id)
    parcel.current_lat = lat
    parcel.current_lon = lon
    parcel.current_address = reverse_geocode(lat, lon)
    db.session.commit()
    return jsonify({"msg": "Location updated"}), 200
