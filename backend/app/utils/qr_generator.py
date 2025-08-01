# backend/app/utils/qr_generator.py

import qrcode
from fpdf import FPDF
import os
from datetime import datetime

def generate_qr_pdf(user_name, delivery_id, payment_id, destination_path='app/static/receipts/'):
    # Ensure directory exists
    os.makedirs(destination_path, exist_ok=True)

    qr_data = f"User: {user_name}\nDelivery ID: {delivery_id}\nPayment ID: {payment_id}\nStatus: PAID"
    qr_img = qrcode.make(qr_data)
    qr_file = os.path.join(destination_path, f"{delivery_id}_qr.png")
    qr_img.save(qr_file)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="Deliveroo Delivery Receipt", ln=True, align='C')

    pdf.set_font("Arial", size=11)
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Customer: {user_name}", ln=True)
    pdf.cell(200, 10, txt=f"Delivery ID: {delivery_id}", ln=True)
    pdf.cell(200, 10, txt=f"Payment ID: {payment_id}", ln=True)
    pdf.cell(200, 10, txt=f"Issue Date: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC", ln=True)

    pdf.image(qr_file, x=80, y=80, w=50, h=50)
    output_path = os.path.join(destination_path, f"{delivery_id}_receipt.pdf")
    pdf.output(output_path)

    return output_path
