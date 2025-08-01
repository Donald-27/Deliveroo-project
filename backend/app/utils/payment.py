# backend/app/utils/payment.py

import stripe
import requests
from flask import current_app
from app.models import Payment
from app import db
from datetime import datetime

stripe.api_key = current_app.config.get('STRIPE_SECRET_KEY')

def process_stripe_payment(amount_cents, currency, description, token, user_id, delivery_id):
    try:
        charge = stripe.Charge.create(
            amount=amount_cents,
            currency=currency,
            description=description,
            source=token
        )

        new_payment = Payment(
            user_id=user_id,
            delivery_id=delivery_id,
            amount=amount_cents / 100,
            currency=currency,
            method='stripe',
            transaction_id=charge.id,
            status='completed',
            created_at=datetime.utcnow()
        )
        db.session.add(new_payment)
        db.session.commit()
        return {'success': True, 'message': 'Stripe payment successful'}
    except stripe.error.StripeError as e:
        return {'success': False, 'message': str(e)}

def process_mpesa_payment(phone_number, amount, user_id, delivery_id):
    # This is just a placeholder – you’ll need Safaricom Daraja API for full implementation.
    # For demonstration, we'll simulate the flow.
    try:
        # Simulate success
        transaction_id = f"MPESA{datetime.utcnow().timestamp()}"
        new_payment = Payment(
            user_id=user_id,
            delivery_id=delivery_id,
            amount=amount,
            currency='KES',
            method='mpesa',
            transaction_id=transaction_id,
            status='completed',
            created_at=datetime.utcnow()
        )
        db.session.add(new_payment)
        db.session.commit()
        return {'success': True, 'message': 'M-Pesa payment successful'}
    except Exception as e:
        return {'success': False, 'message': str(e)}
