from datetime import datetime
from flask_jwt_extended import create_access_token
from extensions import db
from models import User, Student, Company
from utils.enums import Role
from utils.helper import (generate_student_code, generate_company_code)
from utils.response import (success_response, error_response)
from utils.validators import (validate_email, validate_password)
import traceback



class AuthService:

    @staticmethod
    def register_student(data):

        email = data.get("email", "").strip().lower()
        password = data.get("password", "")

        required_fields = ["email", "password"]

        for field in required_fields:
            if not data.get(field):
                return error_response(f"{field.replace('_', ' ').title()} is required.")

        valid, message = validate_email(email)
        if not valid:
            return error_response(message)

        valid, message = validate_password(password)
        if not valid:
            return error_response(message)

        if User.query.filter_by(email=email).first():
            return error_response("Email already exists.")


        try:

            user = User(email=email, role=Role.STUDENT.value)
            user.set_password(password)
            db.session.add(user)
            db.session.flush()

            student = Student(
                student_code=generate_student_code(),
                user_id=user.id,
            )

            db.session.add(student)
            db.session.commit()

            return success_response(
                "Student registered successfully."
            )

        except Exception as e:
            db.session.rollback()
            traceback.print_exc()
            return error_response(str(e), status_code=500)

    @staticmethod
    def register_company(data):

        email = data.get("email", "").strip().lower()
        password = data.get("password", "")

        required_fields = ["email", "password"]

        for field in required_fields:
            if not data.get(field):
                return error_response(f"{field.replace('_', ' ').title()} is required.")

        valid, message = validate_email(email)
        if not valid:
            return error_response(message)

        valid, message = validate_password(password)
        if not valid:
            return error_response(message)

        if User.query.filter_by(email=email).first():
            return error_response("Email already exists.")

        try:

            user = User(email=email, role=Role.COMPANY.value)
            user.set_password(password)
            db.session.add(user)
            db.session.flush()

            company = Company(
                company_code=generate_company_code(),
                user_id=user.id,
            )

            db.session.add(company)
            db.session.commit()

            return success_response(
                "Company registered successfully. Waiting for admin approval."
            )

        except Exception as e:
            db.session.rollback()
            return error_response(str(e), status_code=500)

    @staticmethod
    def login(data):

        email = data.get("email", "").strip().lower()
        password = data.get("password", "")

        user = User.query.filter_by(email=email).first()

        if not user:
            return error_response("Invalid email or password.", status_code=401)

        if not user.check_password(password):
            return error_response("Invalid email or password.", status_code=401)

        if not user.is_active:
            return error_response("Your account has been deactivated.", status_code=403)

        if user.role == Role.COMPANY.value:

            company = Company.query.filter_by(user_id=user.id).first()
            if company and company.status != "Approved":
                return error_response(
                    "Your company account is awaiting admin approval.",
                    status_code=403
                )

        user.last_login = datetime.utcnow()
        db.session.commit()

        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={
                "role": user.role,
                "email":user.email
            }
        )

        return success_response(
            "Login successful.",
            {
                "access_token": access_token,

                "user": {
                    "id": user.id,
                    "email": user.email,
                    "role": user.role
                }
            }
)