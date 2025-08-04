from flask import Blueprint
from routes.parcel_routes import parcel_bp
from routes.admin_routes import admin_bp

def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(parcel_bp, url_prefix='/api/parcels')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
