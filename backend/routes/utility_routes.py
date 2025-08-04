from flask import Blueprint, jsonify

utility_bp = Blueprint("utility_routes", __name__, url_prefix="/api/utils")

@utility_bp.route("/test", methods=["GET"])
def test_utility():
    return jsonify({"message": "Utility route working!"})
