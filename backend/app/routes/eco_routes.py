# backend/app/routes/eco_routes.py

from flask import Blueprint, jsonify, request
from ..models import db, Courier, Parcel
from sqlalchemy import or_

eco_routes = Blueprint("eco_routes", __name__)

@eco_routes.route("/eco/couriers", methods=["GET"])
def get_eco_friendly_couriers():
    eco_vehicles = ["bike", "electric van", "scooter"]
    couriers = Courier.query.filter(
        Courier.vehicle_type.in_(eco_vehicles),
        Courier.is_active == True
    ).all()
    return jsonify([
        {
            "id": c.id,
            "name": c.name,
            "vehicle": c.vehicle_type,
            "rating": c.rating
        } for c in couriers
    ])


@eco_routes.route("/eco/assign/<parcel_id>", methods=["POST"])
def assign_eco_courier(parcel_id):
    eco_vehicles = ["bike", "electric van", "scooter"]
    courier = Courier.query.filter(
        Courier.vehicle_type.in_(eco_vehicles),
        Courier.is_active == True
    ).order_by(Courier.rating.desc()).first()

    if not courier:
        return jsonify({"error": "No eco-friendly courier available"}), 404

    parcel = Parcel.query.get(parcel_id)
    if not parcel:
        return jsonify({"error": "Parcel not found"}), 404

    parcel.courier = courier
    parcel.eco_mode = True
    parcel.status = "assigned"
    db.session.commit()

    return jsonify({"message": f"Eco courier {courier.name} assigned", "courier_id": courier.id})
