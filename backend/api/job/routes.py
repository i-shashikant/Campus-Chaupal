from flask import Blueprint

from services.job_service import JobService

job_bp = Blueprint(
    "jobs",
    __name__,
    url_prefix="/api/jobs"
)


@job_bp.route("", methods=["GET"])
def get_jobs():
    return JobService.get_all_jobs()