from flask import request
from . import auth_bp
from services.auth_service import AuthService


@auth_bp.post("/register/student")
def register_student():

    return AuthService.register_student(
        request.get_json()
    )