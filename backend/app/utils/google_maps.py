# backend/app/utils/google_maps.py

import requests
import os

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def get_distance_and_duration(origin, destination):
    """
    Returns distance in kilometers and duration in minutes between origin and destination
    """
    if not GOOGLE_MAPS_API_KEY:
        raise EnvironmentError("GOOGLE_MAPS_API_KEY not set in environment variables")

    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": origin,
        "destinations": destination,
        "key": GOOGLE_MAPS_API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    try:
        row = data["rows"][0]["elements"][0]
        distance_km = row["distance"]["value"] / 1000  # meters to km
        duration_minutes = row["duration"]["value"] / 60  # seconds to minutes
        return round(distance_km, 2), round(duration_minutes, 2)
    except Exception as e:
        print("Error fetching distance matrix:", e)
        return None, None
