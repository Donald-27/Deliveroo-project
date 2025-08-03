from flask import Blueprint, request
from controllers.admin_controller import (
    get_dashboard_stats,
    get_all_users,
    toggle_user_access
)

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/dashboard-stats', methods=['GET'])
def dashboard_stats():
    return get_dashboard_stats()

@admin_bp.route('/users', methods=['GET'])
def all_users():
    return get_all_users()

@admin_bp.route('/toggle-access/<int:user_id>', methods=['PUT'])
def toggle_access(user_id):
    data = request.get_json()
    return toggle_user_access(user_id, data)
