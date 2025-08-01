# backend/app/config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Flask
    SECRET_KEY            = os.environ.get("SECRET_KEY", "super-secret-key")
    JSONIFY_PRETTYPRINT_REGULAR = True

    # Database
    SQLALCHEMY_DATABASE_URI  = os.environ.get(
        "DATABASE_URL",
        f"sqlite:///{os.path.join(basedir, '../data/dev.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT
    JWT_SECRET_KEY        = os.environ.get("JWT_SECRET_KEY", "jwt-secret-key")
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # seconds

    # Mail (for email/SMS notifications)
    MAIL_SERVER           = os.environ.get("MAIL_SERVER", "smtp.sendgrid.net")
    MAIL_PORT             = int(os.environ.get("MAIL_PORT", "587"))
    MAIL_USE_TLS          = True
    MAIL_USERNAME         = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD         = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER   = os.environ.get("MAIL_DEFAULT_SENDER", "noreply@deliveroo.com")

    # Stripe & M-Pesa
    STRIPE_API_KEY        = os.environ.get("STRIPE_API_KEY")
    MPESA_API_KEY         = os.environ.get("MPESA_API_KEY")
    MPESA_API_SECRET      = os.environ.get("MPESA_API_SECRET")
    MPESA_SHORTCODE       = os.environ.get("MPESA_SHORTCODE")

    # Frontend URL for callback links
    FRONTEND_URL          = os.environ.get("FRONTEND_URL", "http://localhost:3000")
