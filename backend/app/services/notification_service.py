from flask_mail import Message
from app import mail
from flask import current_app

def notify_eta(user_email, eta):
    subject = "Your Parcel ETA"
    sender = current_app.config['MAIL_USERNAME']
    recipients = [user_email]
    body = f"Hello,\n\nYour parcel is expected to arrive at {eta}.\n\nThank you for using Deliveroo!"

    msg = Message(subject=subject, sender=sender, recipients=recipients, body=body)
    mail.send(msg)
