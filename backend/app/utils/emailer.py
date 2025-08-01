# backend/app/utils/emailer.py

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def send_email(to_email, subject, message):
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_USER
        msg["To"] = to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(message, "html"))

        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)
        server.quit()

        print(f"✅ Email sent to {to_email}")
        return True
    except Exception as e:
        print(f"❌ Email failed: {e}")
        return False

def parcel_status_update_email(user_email, parcel_id, new_status):
    subject = f"Parcel #{parcel_id} Status Updated"
    message = f"""
    <h2>Status Update</h2>
    <p>Your parcel <strong>#{parcel_id}</strong> status has been updated to:</p>
    <p style='font-size:18px;color:green'><strong>{new_status}</strong></p>
    <p>Thank you for using <b>Deliveroo</b>.</p>
    """
    send_email(user_email, subject, message)

def parcel_location_update_email(user_email, parcel_id, new_location):
    subject = f"Parcel #{parcel_id} Location Changed"
    message = f"""
    <h2>Location Update</h2>
    <p>Your parcel <strong>#{parcel_id}</strong> has moved to:</p>
    <p style='font-size:18px;color:blue'><strong>{new_location}</strong></p>
    <p>Track it on your dashboard for live updates.</p>
    """
    send_email(user_email, subject, message)
