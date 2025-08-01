# backend/app/utils/tracker.py

from datetime import datetime
from app.models import Parcel, ParcelLocationLog
from app.utils.google_maps import get_distance_and_eta

def update_present_location(parcel_id, location, session):
    parcel = session.query(Parcel).filter_by(id=parcel_id).first()
    if parcel:
        parcel.present_location = location
        parcel.last_updated = datetime.utcnow()

        # Log the location history
        log = ParcelLocationLog(parcel_id=parcel.id, location=location, timestamp=datetime.utcnow())
        session.add(log)

        session.commit()
        return True
    return False

def get_location_history(parcel_id, session):
    logs = (
        session.query(ParcelLocationLog)
        .filter_by(parcel_id=parcel_id)
        .order_by(ParcelLocationLog.timestamp.asc())
        .all()
    )
    return [{"location": log.location, "time": log.timestamp.isoformat()} for log in logs]

def get_eta(parcel, session):
    # Uses current location and destination to calculate ETA
    if parcel.present_location and parcel.destination:
        distance_km, duration_min = get_distance_and_eta(parcel.present_location, parcel.destination)
        return {
            "distance_km": distance_km,
            "estimated_duration_min": duration_min,
        }
    return None
