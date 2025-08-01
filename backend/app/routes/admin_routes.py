# backend/app/routes/admin_routes.py

from flask import Blueprint, jsonify, request
from ..models import db, User, Courier, Parcel, Incident
from datetime import datetime

admin_routes = Blueprint("admin_routes", __name__)

# Get all users
@admin_routes.route("/admin/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([
        {
            "id": u.id,
            "email": u.email,
            "name": u.name,
            "phone": u.phone,
            "created_at": u.created_at
        } for u in users
    ])

# Get all couriers
@admin_routes.route("/admin/couriers", methods=["GET"])
def get_couriers():
    couriers = Courier.query.all()
    return jsonify([
        {
            "id": c.id,
            "name": c.name,
            "phone": c.phone,
            "vehicle": c.vehicle_type,
            "rating": c.rating,
            "active": c.is_active
        } for c in couriers
    ])

# Get all parcels
@admin_routes.route("/admin/parcels", methods=["GET"])
def get_all_parcels():
    parcels = Parcel.query.all()
    return jsonify([
        {
            "id": p.id,
            "user_id": p.user_id,
            "courier_id": getattr(p.courier, "id", None),
            "status": p.status,
            "eco_mode": p.eco_mode,
            "scheduled_at": p.scheduled_at,
            "created_at": p.created_at
        } for p in parcels
    ])

# Deactivate courier
@admin_routes.route("/admin/courier/<courier_id>/deactivate", methods=["POST"])
def deactivate_courier(courier_id):
    courier = Courier.query.get(courier_id)
    if not courier:
        return jsonify({"error": "Courier not found"}), 404

    courier.is_active = False
    db.session.commit()
    return jsonify({"message": "Courier deactivated"})

# View courier performance
@admin_routes.route("/admin/courier/<courier_id>/performance", methods=["GET"])
def courier_performance(courier_id):
    courier = Courier.query.get(courier_id)
    if not courier:
        return jsonify({"error": "Courier not found"}), 404

    delivered = Parcel.query.filter_by(courier=courier, status="delivered").count()
    incidents = Incident.query.filter_by(courier=courier).count()
    return jsonify({
        "courier_id": courier.id,
        "name": courier.name,
        "rating": courier.rating,
        "parcels_delivered": delivered,
        "incidents_reported": incidents
    })

# View all incidents
@admin_routes.route("/admin/incidents", methods=["GET"])
def get_all_incidents():
    incidents = Incident.query.all()
    return jsonify([
        {
            "id": i.id,
            "description": i.description,
            "courier": i.courier.name,
            "parcel_id": i.parcel_id,
            "photo": i.photo_url,
            "created_at": i.created_at
        } for i in incidents
    ])
