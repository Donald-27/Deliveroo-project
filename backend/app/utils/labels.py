# backend/app/utils/labels.py

import qrcode
from fpdf import FPDF
import os
from datetime import datetime

LABELS_DIR = os.path.join(os.getcwd(), "generated_labels")
os.makedirs(LABELS_DIR, exist_ok=True)

class LabelGenerator:
    def __init__(self, parcel_id, sender_name, receiver_name, pickup, destination, weight, status):
        self.parcel_id = parcel_id
        self.sender_name = sender_name
        self.receiver_name = receiver_name
        self.pickup = pickup
        self.destination = destination
        self.weight = weight
        self.status = status

    def generate_qr(self):
        qr = qrcode.make(f"DELIVEROO_PARCEL:{self.parcel_id}")
        qr_path = os.path.join(LABELS_DIR, f"{self.parcel_id}_qr.png")
        qr.save(qr_path)
        return qr_path

    def generate_label_pdf(self):
        qr_path = self.generate_qr()
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Title
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="Deliveroo Parcel Label", ln=True, align="C")
        pdf.set_font("Arial", size=12)

        # Info
        pdf.cell(200, 10, txt=f"Parcel ID: {self.parcel_id}", ln=True)
        pdf.cell(200, 10, txt=f"Sender: {self.sender_name}", ln=True)
        pdf.cell(200, 10, txt=f"Receiver: {self.receiver_name}", ln=True)
        pdf.cell(200, 10, txt=f"Pickup: {self.pickup}", ln=True)
        pdf.cell(200, 10, txt=f"Destination: {self.destination}", ln=True)
        pdf.cell(200, 10, txt=f"Weight: {self.weight} kg", ln=True)
        pdf.cell(200, 10, txt=f"Status: {self.status}", ln=True)
        pdf.cell(200, 10, txt=f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)

        # QR Code
        pdf.image(qr_path, x=80, y=None, w=50)

        # Save
        label_path = os.path.join(LABELS_DIR, f"{self.parcel_id}_label.pdf")
        pdf.output(label_path)

        return label_path
