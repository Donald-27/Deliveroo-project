import os
from flask import Flask
from flask_cors import CORS
from .database import db
from flask_jwt_extended import JWTManager
from .routes.auth_routes import auth_bp
from .routes.parcel_routes import parcel_bp
from .routes.admin_routes import admin_bp
from .routes.utils_routes import utils_bp
from config import Config

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)

    # create upload folder
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(parcel_bp, url_prefix='/api/parcels')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    app.register_blueprint(utils_bp, url_prefix='/api/utils')

    with app.app_context():
        db.create_all()

    return app
