from flask import Blueprint, request
from flask_security import auth_required, roles_required, current_user
from services.student_service import StudentService

import os

from utils.response import success_response


student_bp = Blueprint(
    "student",
    __name__,
    url_prefix="/api/student",
)


@student_bp.route("/profile", methods=["GET"])
@auth_required("token")
@roles_required("student")
def get_profile():
    return StudentService.get_profile(current_user.id)


@student_bp.route("/profile", methods=["PUT"])
@auth_required("token")
@roles_required("student")
def update_profile():
    data = request.get_json()
    return StudentService.update_profile(current_user.id, data)

@student_bp.post("/resume")
@auth_required("token")
@roles_required("student")
def upload_resume():

    return StudentService.upload_resume(
        current_user.id,
        request.files.get("resume")
    )
