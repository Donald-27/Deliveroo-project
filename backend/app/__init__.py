from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_cors import CORS
from .config import Config

# Initialize extensions
db = SQLAlchemy()
jwt = JWTManager()
mail = Mail()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__, static_folder="../frontend/dist", static_url_path="/")
    app.config.from_object(config_class)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    db.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from .routes.auth       import auth_bp
    from .routes.parcel     import parcel_bp
    from .routes.tracking   import tracking_bp
    from .routes.referrals  import referrals_bp
    from .routes.templates  import templates_bp
    from .routes.courier    import courier_bp
    from .routes.admin      import admin_bp

    app.register_blueprint(auth_bp,       url_prefix="/api/auth")
    app.register_blueprint(parcel_bp,     url_prefix="/api/parcels")
    app.register_blueprint(tracking_bp,   url_prefix="/api/tracking")
    app.register_blueprint(referrals_bp,  url_prefix="/api/referrals")
    app.register_blueprint(templates_bp,  url_prefix="/api/templates")
    app.register_blueprint(courier_bp,    url_prefix="/api/courier")
    app.register_blueprint(admin_bp,      url_prefix="/api/admin")

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def serve_frontend(path):
        return app.send_static_file("index.html")

    return app
