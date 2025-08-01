# backend/app/routes/incident_routes.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from app.models import Incident, Parcel, User, db

incident_bp = Blueprint('incidents', __name__, url_prefix='/api/incidents')


# Report an incident
@incident_bp.route('/report/<int:parcel_id>', methods=['POST'])
@jwt_required()
def report_incident(parcel_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if user.role not in ['courier', 'admin']:
        return jsonify({'error': 'Only couriers or admins can report incidents'}), 403

    parcel = Parcel.query.get(parcel_id)
    if not parcel:
        return jsonify({'error': 'Parcel not found'}), 404

    data = request.get_json()
    description = data.get('description', '')

    if not description:
        return jsonify({'error': 'Description is required'}), 400

    incident = Incident(
        parcel_id=parcel_id,
        reporter_id=user_id,
        description=description,
        timestamp=datetime.utcnow()
    )

    db.session.add(incident)
    db.session.commit()

    return jsonify({'message': 'Incident reported successfully'}), 201


# Get all incidents for a specific parcel
@incident_bp.route('/parcel/<int:parcel_id>', methods=['GET'])
@jwt_required()
def get_parcel_incidents(parcel_id):
    incidents = Incident.query.filter_by(parcel_id=parcel_id).order_by(Incident.timestamp.desc()).all()
    return jsonify([
        {
            'id': i.id,
            'parcel_id': i.parcel_id,
            'reporter_id': i.reporter_id,
            'reporter_name': i.reporter.name,
            'description': i.description,
            'timestamp': i.timestamp.isoformat()
        }
        for i in incidents
    ])

