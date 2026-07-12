from flask import Blueprint, request
from flask_security import auth_required, roles_required, current_user

from services.job_service import JobService

company_bp = Blueprint(
    "company",
    __name__,
    url_prefix="/api/company"
)


@company_bp.route("/jobs", methods=["POST"])
@auth_required("token")
@roles_required("company")
def create_job():

    return JobService.create_job(
        current_user.company.id,
        request.get_json()
    )