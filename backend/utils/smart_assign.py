def smart_assign(parcels, couriers):
    assigned = []
    unassigned = parcels.copy()

    for courier in couriers:
        for parcel in unassigned:
            if courier['region'] == parcel['destination_region']:
                assigned.append({
                    "courier_id": courier['id'],
                    "parcel_id": parcel['id']
                })
                unassigned.remove(parcel)
                break

    return {"assigned": assigned, "unassigned": [p['id'] for p in unassigned]}
