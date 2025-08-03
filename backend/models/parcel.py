from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Parcel(db.Model):
    __tablename__ = 'parcels'

    id = db.Column(db.Integer, primary_key=True)
    sender_name = db.Column(db.String(120), nullable=False)
    sender_phone = db.Column(db.String(20), nullable=False)
    receiver_name = db.Column(db.String(120), nullable=False)
    receiver_phone = db.Column(db.String(20), nullable=False)
    pickup_address = db.Column(db.String(255), nullable=False)
    delivery_address = db.Column(db.String(255), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='Pending')
    eco_mode = db.Column(db.Boolean, default=False)
    courier_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    delivery_time = db.Column(db.String(50), nullable=True)
    qr_code_path = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'sender_name': self.sender_name,
            'sender_phone': self.sender_phone,
            'receiver_name': self.receiver_name,
            'receiver_phone': self.receiver_phone,
            'pickup_address': self.pickup_address,
            'delivery_address': self.delivery_address,
            'weight': self.weight,
            'status': self.status,
            'eco_mode': self.eco_mode,
            'courier_id': self.courier_id,
            'delivery_time': self.delivery_time,
            'qr_code_path': self.qr_code_path,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
