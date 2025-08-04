def assign_courier(pickup_address, delivery_address):
    """
    Dummy courier assignment logic based on delivery address region.
    Returns courier_id or None.
    """

    address = delivery_address.lower()

    couriers = [
        {"id": 1, "region": "nairobi"},
        {"id": 2, "region": "mombasa"},
        {"id": 3, "region": "kisumu"}
    ]

    for courier in couriers:
        if courier['region'] in address:
            return courier['id']


    return None
