from flask import Blueprint

from flask_security import (
    auth_required,
    roles_required,
    current_user
)

from services.application_service import ApplicationService

application_bp = Blueprint(

    "applications",

    __name__,

    url_prefix="/api/applications"

)


@application_bp.route("/apply/<int:job_id>", methods=["POST"])
@auth_required("token")
@roles_required("student")

def apply(job_id):

    return ApplicationService.apply(

        current_user.student.id,

        job_id

    )


@application_bp.route("/student", methods=["GET"])
@auth_required("token")
@roles_required("student")

def student_apps():

    return ApplicationService.student_applications(

        current_user.student.id

    )


@application_bp.route("/company", methods=["GET"])
@auth_required("token")
@roles_required("company")

def company_apps():

    return ApplicationService.company_applications(

        current_user.company.id

    )