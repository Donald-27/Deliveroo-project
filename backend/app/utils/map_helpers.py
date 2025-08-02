from geopy.geocoders import Nominatim

def get_coordinates(address):
    geolocator = Nominatim(user_agent="deliveroo-courier")
    location = geolocator.geocode(address)
    if location:
        return {'lat': location.latitude, 'lng': location.longitude}
    return {'error': 'Address not found'}
