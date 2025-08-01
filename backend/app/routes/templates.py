# backend/app/routes/templates.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .. import db
from ..models import Template

templates_bp = Blueprint("templates", __name__)

@templates_bp.route("/", methods=["GET"])
@jwt_required()
def list_templates():
    user_id = get_jwt_identity()
    templates = Template.query.filter_by(user_id=user_id).all()
    return jsonify([t.to_dict() for t in templates]), 200

@templates_bp.route("/", methods=["POST"])
@jwt_required()
def create_template():
    user_id = get_jwt_identity()
    data = request.get_json()
    name = data.get("name")
    template_data = data.get("data")  # expect JSON of parcel fields

    tmpl = Template(user_id=user_id, name=name, data=template_data)
    db.session.add(tmpl)
    db.session.commit()
    return jsonify(tmpl.to_dict()), 201

@templates_bp.route("/<template_id>", methods=["PUT"])
@jwt_required()
def update_template(template_id):
    user_id = get_jwt_identity()
    tmpl = Template.query.filter_by(id=template_id, user_id=user_id).first_or_404()
    data = request.get_json()
    tmpl.name = data.get("name", tmpl.name)
    tmpl.data = data.get("data", tmpl.data)
    db.session.commit()
    return jsonify(tmpl.to_dict()), 200

@templates_bp.route("/<template_id>", methods=["DELETE"])
@jwt_required()
def delete_template(template_id):
    user_id = get_jwt_identity()
    tmpl = Template.query.filter_by(id=template_id, user_id=user_id).first_or_404()
    db.session.delete(tmpl)
    db.session.commit()
    return jsonify({"msg": "Template deleted"}), 200
