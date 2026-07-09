from datetime import datetime
from flask_jwt_extended import create_access_token
from extensions import db
from models import User, Student, Company
from utils.enums import Role
from utils.helper import (generate_student_code, generate_company_code)
from utils.response import (success_response, error_response)
from utils.validators import (validate_email, validate_password)



class AuthService:

    @staticmethod
    def register_student(data):

        email = data.get("email", "").strip().lower()
        password = data.get("password", "")

        required_fields = ["full_name", "roll_number", "branch", "year"]

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

        if Student.query.filter_by(
            roll_number=data.get("roll_number")
        ).first():
            return error_response("Roll number already exists.")

        try:

            user = User(email=email, role=Role.STUDENT.value)
            user.set_password(password)
            db.session.add(user)
            db.session.flush()

            student = Student(
                student_code=generate_student_code(),
                user_id=user.id,
                full_name=data.get("full_name").strip(),
                roll_number=data.get("roll_number").strip(),
                branch=data.get("branch").strip(),
                year=data.get("year"),
                cgpa=data.get("cgpa"),
                graduation_year=data.get("graduation_year"),
                gender=data.get("gender"),
                phone=data.get("phone"),
                address=data.get("address")
            )

            db.session.add(student)
            db.session.commit()

            return success_response(
                "Student registered successfully."
            )

        except Exception as e:
            db.session.rollback()
            return error_response(str(e), status_code=500)

    @staticmethod
    def register_company(data):

        email = data.get("email", "").strip().lower()
        password = data.get("password", "")

        required_fields = ["company_name", "industry", "hr_name"]

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
                company_name=data.get("company_name"),
                industry=data.get("industry"),
                website=data.get("website"),
                description=data.get("description"),
                address=data.get("address"),
                city=data.get("city"),
                state=data.get("state"),
                country=data.get("country"),
                logo=data.get("logo"),
                hr_name=data.get("hr_name"),
                hr_email=data.get("hr_email"),
                phone=data.get("phone")
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
                "role": user.role
            }
        )

        return success_response(
            "Login successful.",
            {
                "access_token": access_token,
                "role": user.role,
                "user_id": user.id
            }
        )