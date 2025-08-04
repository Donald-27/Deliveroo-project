from flask import Blueprint, request, jsonify
from controllers.user_controller import get_all_users, get_user, update_user, delete_user

user_bp = Blueprint("user_routes", __name__, url_prefix="/api/user")

@user_bp.route("/test", methods=["GET"])
def test_user_route():
    return jsonify({"message": "User route working"}), 200


@user_bp.route("/", methods=["GET"])
def handle_get_all_users():
    return get_all_users()


@user_bp.route("/<int:user_id>", methods=["GET"])
def handle_get_user(user_id):
    return get_user(user_id)


@user_bp.route("/<int:user_id>", methods=["PUT"])
def handle_update_user(user_id):
    return update_user(user_id=user_id)


@user_bp.route("/<int:user_id>", methods=["DELETE"])
def handle_delete_user(user_id):
    return delete_user(user_id=user_id)
