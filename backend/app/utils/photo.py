import os
import uuid
from PIL import Image
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "app/static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_proof_photo(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        ext = filename.rsplit(".", 1)[1].lower()
        unique_filename = f"{uuid.uuid4().hex}.{ext}"
        filepath = os.path.join(UPLOAD_FOLDER, unique_filename)

        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        file.save(filepath)

        generate_thumbnail(filepath)
        return unique_filename
    return None

def generate_thumbnail(image_path, size=(300, 300)):
    thumb_path = image_path.replace(".", "_thumb.")
    try:
        img = Image.open(image_path)
        img.thumbnail(size)
        img.save(thumb_path)
    except Exception as e:
        print("Thumbnail generation failed:", e)
