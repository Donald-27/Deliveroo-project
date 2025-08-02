import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.getenv("JWT_SECRET_KEY", "supersecretkey")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///deliveroo.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = SECRET_KEY
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'app', 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
