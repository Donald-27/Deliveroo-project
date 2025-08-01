def assign_courier_to_parcel(parcel, couriers):
    """
    Assign the best available courier to the parcel based on proximity or load.
    """
    if not couriers:
        return None

    # Simplified smart assignment: pick the courier with the fewest parcels
    sorted_couriers = sorted(couriers, key=lambda c: c.get('assigned_parcels', 0))
    return sorted_couriers[0]
