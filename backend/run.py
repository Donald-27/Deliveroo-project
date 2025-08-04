from flask import Flask
from config import Config
from extensions import db, jwt
from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
from routes.parcel_routes import parcel_bp
from routes.admin_routes import admin_bp
from routes.utility_routes import utility_bp
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(user_bp, url_prefix="/api/user")
    app.register_blueprint(parcel_bp, url_prefix="/api/parcels") 
    app.register_blueprint(admin_bp, url_prefix="/api/admin")
    app.register_blueprint(utility_bp, url_prefix="/api/utils")

    return app

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
