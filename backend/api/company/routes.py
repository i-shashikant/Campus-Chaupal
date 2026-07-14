from flask import Blueprint, request
from flask_security import auth_required, roles_required, current_user

from services.job_service import JobService
from services.application_service import ApplicationService
from services.company_service import CompanyService


company_bp = Blueprint(
    "company",
    __name__,
    url_prefix="/api/company"
)


@company_bp.route("/jobs", methods=["GET"])
@auth_required("token")
@roles_required("company")
def my_jobs():
    return JobService.get_company_jobs(current_user.company.id)


@company_bp.route("/jobs", methods=["POST"])
@auth_required("token")
@roles_required("company")
def create_job():
    return JobService.create_job(
        current_user.company.id,
        request.get_json()
    )


@company_bp.route("/jobs/<int:job_id>", methods=["PUT"])
@auth_required("token")
@roles_required("company")
def update_job(job_id):
    return JobService.update_job(
        current_user.company.id,
        job_id,
        request.get_json()
    )


@company_bp.route("/jobs/<int:job_id>", methods=["DELETE"])
@auth_required("token")
@roles_required("company")
def delete_job(job_id):
    return JobService.delete_job(
        current_user.company.id,
        job_id
    )

@company_bp.route("/jobs/<int:job_id>/close", methods=["PUT"])
@auth_required("token")
@roles_required("company")
def close_job(job_id):
    return JobService.close_job(
        current_user.company.id,
        job_id
    )


@company_bp.route(
    "/applications/<int:application_id>/status",
    methods=["PUT"]
)


@auth_required("token")
@roles_required("company")
def update_application_status(application_id):

    return ApplicationService.update_application_status(
        current_user.company.id,
        application_id,
        request.get_json()
    )


@company_bp.get("/profile")
@auth_required("token")
@roles_required("company")
def get_profile():
    return CompanyService.get_profile(current_user.id)




@company_bp.put("/profile")
@auth_required("token")
@roles_required("company")
def update_profile():
    return CompanyService.update_profile(
        current_user.id,
        request.get_json()
    )


@company_bp.post("/logo")
@auth_required("token")
@roles_required("company")
def upload_logo():

    return CompanyService.upload_logo(
        current_user.id,
        request.files
    )

@company_bp.put("/applications/<int:application_id>/interview")
@auth_required("token")
@roles_required("company")
def schedule_interview(application_id):

    return ApplicationService.schedule_interview(
        application_id,
        request.get_json()
    )