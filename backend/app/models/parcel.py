from ..database import db
from datetime import datetime

class Parcel(db.Model):
    __tablename__ = 'parcels'

    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    recipient_name = db.Column(db.String(120), nullable=False)
    recipient_address = db.Column(db.String(255), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='Pending')  # e.g., Pending, In Transit, Delivered
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Parcel {self.id}>'
