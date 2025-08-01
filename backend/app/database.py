# backend/app/database.py

from . import db

def init_db():
    """
    Call this in a Flask CLI command or migration to create tables.
    """
    db.create_all()
