from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from config import Config
from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
from routes.parcel_routes import parcel_bp
from routes.admin_routes import admin_bp
from routes.utility_routes import utility_bp

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
jwt = JWTManager(app)
CORS(app)

app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(user_bp, url_prefix="/api/user")
app.register_blueprint(parcel_bp, url_prefix="/api/parcel")
app.register_blueprint(admin_bp, url_prefix="/api/admin")
app.register_blueprint(utility_bp, url_prefix="/api/utils")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
