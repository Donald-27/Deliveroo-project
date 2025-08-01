# backend/app/routes/tracking.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .. import db
from ..models import Parcel, TimelineEvent, Courier
from ..services.notification_service import notify_eta

tracking_bp = Blueprint("tracking", __name__)

@tracking_bp.route("/<parcel_id>/timeline", methods=["GET"])
@jwt_required()
def get_timeline(parcel_id):
    user_id = get_jwt_identity()
    parcel = Parcel.query.filter_by(id=parcel_id, user_id=user_id).first_or_404()
    events = TimelineEvent.query.filter_by(parcel_id=parcel.id).order_by(TimelineEvent.created_at).all()
    return jsonify([e.to_dict() for e in events]), 200

@tracking_bp.route("/<parcel_id>/event", methods=["POST"])
@jwt_required()
def add_event(parcel_id):
    """
    Admin or Courier can push a new timeline event (e.g., picked up, in transit).
    """
    data = request.get_json()
    status = data.get("status")
    note = data.get("note", "")
    parcel = Parcel.query.get_or_404(parcel_id)

    # Only allow if courier or admin (you can add role checks here)
    event = TimelineEvent(parcel_id=parcel.id, status=status, note=note)
    db.session.add(event)
    db.session.commit()

    # Optionally send notification to user
    notify_eta(parcel, status)

    return jsonify(event.to_dict()), 201

@tracking_bp.route("/<parcel_id>/location", methods=["GET"])
@jwt_required(optional=True)
def get_courier_location(parcel_id):
    """
    Returns the last known location of the courier for display on the map.
    Public: allows recipients without JWT to view if they have the link.
    """
    parcel = Parcel.query.get_or_404(parcel_id)
    courier = Courier.query.get(parcel.courier_id)
    if not courier or not courier.is_active:
        return jsonify({"msg": "Courier not available"}), 404

    return jsonify({
        "lat": courier.last_latitude,
        "lng": courier.last_longitude,
        "updated_at": courier.updated_at.isoformat()
    }), 200

@tracking_bp.route("/<parcel_id>/eta-subscribe", methods=["POST"])
@jwt_required()
def eta_subscribe(parcel_id):
    """
    User can subscribe to ETA alerts for their parcel.
    """
    user_id = get_jwt_identity()
    data = request.get_json()
    channel = data.get("channel")  # 'email' or 'sms'
    # Store subscription in DB or call notification service directly
    notify_eta.subscribe(user_id=user_id, parcel_id=parcel_id, channel=channel)
    return jsonify({"msg": f"Subscribed to ETA alerts via {channel}"}), 200
