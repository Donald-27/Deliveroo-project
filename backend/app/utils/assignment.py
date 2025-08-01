# backend/app/utils/assignment.py

from ..models import Courier, Parcel
from .. import db
from sqlalchemy import func
from datetime import datetime, timedelta
import random

def smart_assign_courier(parcel):
    """
    Assigns a courier based on:
    - Proximity (mocked for now)
    - Current load (fewest assigned parcels)
    - Performance score
    """

    available_couriers = Courier.query.filter_by(active=True).all()

    if not available_couriers:
        return False

    # Score couriers based on workload and performance
    scored = []
    for courier in available_couriers:
        active_parcels = Parcel.query.filter_by(courier_id=courier.id).filter(Parcel.status != "Delivered").count()
        score = courier.performance_score - active_parcels * 2  # prefer low load & high score
        scored.append((courier, score))

    # Sort by score descending
    scored.sort(key=lambda x: x[1], reverse=True)

    top = scored[0][0]
    parcel.courier_id = top.id
    parcel.status = "In Transit"
    db.session.commit()
    return True
