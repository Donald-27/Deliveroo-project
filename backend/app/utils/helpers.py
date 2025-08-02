import qrcode
import os
from uuid import uuid4
from flask import current_app

def generate_qr_code(data):
    if not os.path.exists(current_app.config['UPLOAD_FOLDER']):
        os.makedirs(current_app.config['UPLOAD_FOLDER'])

    qr = qrcode.make(data)
    filename = f"{uuid4().hex}.png"
    path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    qr.save(path)
    return filename
