from flask import Blueprint, request
from flask_security import auth_required, roles_required, current_user

from services.job_service import JobService
from services.application_service import ApplicationService


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