from flask_security import auth_required, roles_required

from . import admin_bp
from services.admin_service import AdminService


@admin_bp.get("/dashboard")
@auth_required("token")
@roles_required("admin")
def dashboard():
    return AdminService.dashboard()

@admin_bp.get("/companies/pending")
@auth_required("token")
@roles_required("admin")
def pending_companies():
    return AdminService.pending_companies()


@admin_bp.put("/company/<int:company_id>/approve")
@auth_required("token")
@roles_required("admin")
def approve_company(company_id):
    return AdminService.approve_company(company_id)


@admin_bp.put("/company/<int:company_id>/reject")
@auth_required("token")
@roles_required("admin")
def reject_company(company_id):
    return AdminService.reject_company(company_id)

@admin_bp.get("/users")
@auth_required("token")
@roles_required("admin")
def users():
    return AdminService.get_users()


@admin_bp.get("/jobs")
@auth_required("token")
@roles_required("admin")
def jobs():
    return AdminService.get_jobs()


@admin_bp.get("/applications")
@auth_required("token")
@roles_required("admin")
def applications():
    return AdminService.get_applications()