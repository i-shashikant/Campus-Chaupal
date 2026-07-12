from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.student_service import StudentService

student_bp = Blueprint(
    "student",
    __name__,
    url_prefix="/api/student"
)


@student_bp.route("/profile", methods=["GET"])
@jwt_required()
def get_profile():

    user_id = int(get_jwt_identity())

    return StudentService.get_profile(user_id)


@student_bp.route("/profile", methods=["PUT"])
@jwt_required()
def update_profile():

    user_id = int(get_jwt_identity())

    data = request.get_json()

    return StudentService.update_profile(user_id, data)