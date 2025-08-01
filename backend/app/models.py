# backend/app/models.py

from datetime import datetime
import uuid
from . import db


def generate_uuid():
    return str(uuid.uuid4())


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(80))
    phone = db.Column(db.String(20))
    referral_code = db.Column(db.String(10), unique=True)
    loyalty_points = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    addresses = db.relationship("Address", backref="user", lazy="dynamic")
    templates = db.relationship("Template", backref="user", lazy="dynamic")
    parcels = db.relationship("Parcel", backref="user", lazy="dynamic")
    referrals_sent = db.relationship("Referral", foreign_keys="Referral.inviter_id", backref="inviter", lazy="dynamic")
    referrals_received = db.relationship("Referral", foreign_keys="Referral.invitee_id", backref="invitee", lazy="dynamic")
    payments = db.relationship("Payment", backref="user", lazy="dynamic")


class Address(db.Model):
    __tablename__ = "addresses"
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    user_id = db.Column(db.String, db.ForeignKey("users.id"), nullable=False)
    label = db.Column(db.String(50))  # e.g., 'Home', 'Office'
    street = db.Column(db.String(120))
    city = db.Column(db.String(50))
    country = db.Column(db.String(50))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)


class Template(db.Model):
    __tablename__ = "templates"
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    user_id = db.Column(db.String, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(50))
    data = db.Column(db.JSON)  # Stores parcel fields for quick reuse


class Referral(db.Model):
    __tablename__ = "referrals"
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    inviter_id = db.Column(db.String, db.ForeignKey("users.id"), nullable=False)
    invitee_id = db.Column(db.String, db.ForeignKey("users.id"), nullable=True)
    code = db.Column(db.String(10), unique=True, nullable=False)
    used = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Courier(db.Model):
    __tablename__ = "couriers"
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    name = db.Column(db.String(80))
    phone = db.Column(db.String(20))
    vehicle_type = db.Column(db.String(20))  # 'bike', 'car', 'van', etc.
    rating = db.Column(db.Float, default=5.0)
    is_active = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    assignments = db.relationship("Parcel", backref="courier", lazy="dynamic")
    incidents = db.relationship("Incident", backref="courier", lazy="dynamic")


class Parcel(db.Model):
    __tablename__ = "parcels"
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    user_id = db.Column(db.String, db.ForeignKey("users.id"), nullable=False)
    courier_id = db.Column(db.String, db.ForeignKey("couriers.id"), nullable=True)
    bulk_id = db.Column(db.String, nullable=True)  # for bulk bookings
    origin_id = db.Column(db.String, db.ForeignKey("addresses.id"))
    destination_id = db.Column(db.String, db.ForeignKey("addresses.id"))
    weight_kg = db.Column(db.Float)
    eco_mode = db.Column(db.Boolean, default=False)
    scheduled_at = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(20), default="created")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    origin = db.relationship("Address", foreign_keys=[origin_id])
    destination = db.relationship("Address", foreign_keys=[destination_id])
    timeline_events = db.relationship("TimelineEvent", backref="parcel", lazy="dynamic")
    payment = db.relationship("Payment", uselist=False, backref="parcel")
    incidents = db.relationship("Incident", backref="parcel", lazy="dynamic")


class Payment(db.Model):
    __tablename__ = "payments"
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    parcel_id = db.Column(db.String, db.ForeignKey("parcels.id"), nullable=False)
    user_id = db.Column(db.String, db.ForeignKey("users.id"), nullable=False)
    method = db.Column(db.String(20))  # 'stripe', 'mpesa'
    amount = db.Column(db.Float)
    tip_amount = db.Column(db.Float, default=0.0)
    insurance_fee = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class TimelineEvent(db.Model):
    __tablename__ = "timeline_events"
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    parcel_id = db.Column(db.String, db.ForeignKey("parcels.id"), nullable=False)
    status = db.Column(db.String(30))
    note = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Incident(db.Model):
    __tablename__ = "incidents"
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    parcel_id = db.Column(db.String, db.ForeignKey("parcels.id"), nullable=False)
    courier_id = db.Column(db.String, db.ForeignKey("couriers.id"), nullable=False)
    description = db.Column(db.String(200))
    photo_url = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    courier_id = db.Column(db.Integer, db.ForeignKey('courier.id'), nullable=False)
    deliveries_completed = db.Column(db.Integer, default=0)
    rating = db.Column(db.Float, default=5.0)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    courier = db.relationship('Courier', backref=db.backref('performance', uselist=False))
