# backend/app/utils/smart_assigner.py

from app.models import Courier, Parcel
from sqlalchemy import func
from geopy.distance import geodesic

def get_coordinates(address):
    # Placeholder for real geocoding logic (e.g., Google Geocoding API)
    return (0.0, 0.0)  # You’ll later plug actual coordinates from maps API

def calculate_distance(loc1, loc2):
    return geodesic(loc1, loc2).km

def find_best_courier(parcel_pickup_location, session):
    best_courier = None
    lowest_score = float('inf')

    pickup_coords = get_coordinates(parcel_pickup_location)
    couriers = session.query(Courier).filter(Courier.status == "available").all()

    for courier in couriers:
        courier_coords = (courier.latitude, courier.longitude)
        distance = calculate_distance(pickup_coords, courier_coords)
        active_parcels = session.query(func.count(Parcel.id)).filter_by(courier_id=courier.id, status="in_transit").scalar()
        urgency_penalty = 1.5 if courier.priority_only else 1

        score = (distance * 0.6) + (active_parcels * 1.2) * urgency_penalty

        if score < lowest_score:
            lowest_score = score
            best_courier = courier

    return best_courier
