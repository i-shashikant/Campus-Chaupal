from flask import request
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


@admin_bp.get("/companies")
@auth_required("token")
@roles_required("admin")
def companies():
    return AdminService.get_companies()


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


@admin_bp.put("/company/<int:company_id>/blacklist")
@auth_required("token")
@roles_required("admin")
def blacklist_company(company_id):
    return AdminService.blacklist_company(company_id)


@admin_bp.put("/company/<int:company_id>/unblock")
@auth_required("token")
@roles_required("admin")
def unblock_company(company_id):
    return AdminService.unblock_company(company_id)


@admin_bp.get("/users")
@auth_required("token")
@roles_required("admin")
def users():
    return AdminService.get_users()


@admin_bp.put("/student/<int:student_id>/blacklist")
@auth_required("token")
@roles_required("admin")
def blacklist_student(student_id):
    return AdminService.blacklist_student(student_id)


@admin_bp.put("/student/<int:student_id>/unblock")
@auth_required("token")
@roles_required("admin")
def unblock_student(student_id):
    return AdminService.unblock_student(student_id)


@admin_bp.get("/jobs")
@auth_required("token")
@roles_required("admin")
def jobs():
    return AdminService.get_jobs()


@admin_bp.get("/jobs/pending")
@auth_required("token")
@roles_required("admin")
def pending_jobs():
    return AdminService.pending_jobs()


@admin_bp.put("/job/<int:job_id>/approve")
@auth_required("token")
@roles_required("admin")
def approve_job(job_id):
    return AdminService.approve_job(job_id)


@admin_bp.put("/job/<int:job_id>/reject")
@auth_required("token")
@roles_required("admin")
def reject_job(job_id):
    data = request.get_json(silent=True) or {}
    return AdminService.reject_job(job_id, data.get("reason"))


@admin_bp.get("/applications")
@auth_required("token")
@roles_required("admin")
def applications():
    return AdminService.get_applications()