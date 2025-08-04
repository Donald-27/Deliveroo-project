import logging
from flask import jsonify
from models.parcel import Parcel
from utils.smart_assign import assign_courier
from extensions import db

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def create_parcel(data):
    try:
        logger.debug(f"Received parcel data: {data}")
        sender_name = data.get('senderName')
        sender_phone = data.get('senderPhone')
        receiver_name = data.get('receiverName')
        receiver_phone = data.get('receiverPhone')
        pickup_address = data.get('pickupAddress')
        delivery_address = data.get('deliveryAddress')
        weight = data.get('parcelWeight')
        description = data.get('parcelDescription')
        delivery_type = data.get('deliveryType', 'standard')
        if not all([sender_name, sender_phone, receiver_name, receiver_phone,
                    pickup_address, delivery_address, weight, description]):
            return jsonify({'error': 'All fields are required'}), 400
        eco_mode = delivery_type.lower() == 'eco'
        courier_id = assign_courier(pickup_address, delivery_address)
        new_parcel = Parcel(
            sender_name=sender_name,
            sender_phone=sender_phone,
            receiver_name=receiver_name,
            receiver_phone=receiver_phone,
            pickup_address=pickup_address,
            delivery_address=delivery_address,
            weight=float(weight),
            eco_mode=eco_mode,
            courier_id=courier_id
        )
        db.session.add(new_parcel)
        db.session.commit()
        logger.debug(f"Parcel created with ID: {new_parcel.id}")
        return jsonify({
            'message': 'Parcel created successfully',
            'parcelId': new_parcel.id,
            'parcel': new_parcel.to_dict()
        }), 201
    except Exception as e:
        logger.error(f"Exception in create_parcel: {str(e)}", exc_info=True)
        return jsonify({'error': str(e)}), 500

def get_all_parcels():
    try:
        parcels = Parcel.query.all()
        return jsonify([parcel.to_dict() for parcel in parcels]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_parcel_by_id(parcel_id):
    try:
        parcel = Parcel.query.get(parcel_id)
        if parcel:
            return jsonify(parcel.to_dict()), 200
        return jsonify({'error': 'Parcel not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def update_parcel_status(parcel_id, data):
    try:
        status = data.get('status')
        parcel = Parcel.query.get(parcel_id)
        if not parcel:
            return jsonify({'error': 'Parcel not found'}), 404
        parcel.status = status
        db.session.commit()
        return jsonify({'message': 'Parcel status updated'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_user_parcels(user_id):
    try:
        parcels = Parcel.query.filter_by(sender_id=user_id).all()
        return jsonify([p.to_dict() for p in parcels]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def track_parcel(parcel_id):
    try:
        parcel = Parcel.query.get(parcel_id)
        if parcel:
            return jsonify({
                'status': parcel.status,
                'location': parcel.current_location or "In Transit"
            }), 200
        return jsonify({'error': 'Parcel not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
