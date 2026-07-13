from flask_security import auth_required, roles_required

from . import admin_bp
from services.admin_service import AdminService


@admin_bp.get("/dashboard")
@auth_required("token")
@roles_required("admin")
def dashboard():
    return AdminService.dashboard()