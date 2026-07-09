from models import User, Student
from extensions import db
from utils.helper import generate_student_code
from utils.validators import (validate_email, validate_password)
from utils.response import (success_response, error_response)
from utils.enums import Role


class AuthService:

    @staticmethod
    def register_student(data):

        email = data.get("email")
        password = data.get("password")

        valid, message = validate_email(email)
        if not valid:
            return error_response(message)

        valid, message = validate_password(password)
        if not valid:
            return error_response(message)

        if User.query.filter_by(email=email).first():
            return error_response("Email already exists.")

        user = User(
            email=email,
            role=Role.STUDENT.value
        )

        user.set_password(password)
        db.session.add(user)
        db.session.flush()

        student = Student(
            student_code=generate_student_code(),
            user_id=user.id,
            full_name=data.get("full_name"),
            roll_number=data.get("roll_number"),
            branch=data.get("branch"),
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