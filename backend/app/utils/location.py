# backend/app/utils/location.py

import requests
import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
DISTANCE_URL = "https://maps.googleapis.com/maps/api/distancematrix/json"

def reverse_geocode(lat, lon):
    params = {
        "latlng": f"{lat},{lon}",
        "key": GOOGLE_API_KEY
    }
    resp = requests.get(GEOCODE_URL, params=params)
    data = resp.json()
    if data["status"] == "OK":
        return data["results"][0]["formatted_address"]
    return None

def calculate_distance_and_eta(origin, destination):
    """
    origin & destination: addresses or "lat,lng"
    returns: (distance_text, duration_text, distance_meters, duration_seconds)
    """
    params = {
        "origins": origin,
        "destinations": destination,
        "key": GOOGLE_API_KEY
    }
    resp = requests.get(DISTANCE_URL, params=params)
    data = resp.json()
    if data["status"] == "OK":
        row = data["rows"][0]["elements"][0]
        return (
            row["distance"]["text"],
            row["duration"]["text"],
            row["distance"]["value"],
            row["duration"]["value"]
        )
    return None, None, 0, 0

def generate_map_link(origin, destination):
    return f"https://www.google.com/maps/dir/{origin}/{destination}"
