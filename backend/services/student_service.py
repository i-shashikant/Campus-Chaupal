from extensions import db
from models import User, Student
from utils.response import success_response, error_response

import os
from werkzeug.utils import secure_filename
from flask import current_app
from extensions import cache

class StudentService:

    @staticmethod
    @cache.memoize(timeout=60)
    def get_profile(user_id):

        student = Student.query.filter_by(user_id=user_id).first()

        if not student:
            return error_response("Student not found.", 404)

        return success_response(
            "Profile fetched successfully.",
            {
                "student_code": student.student_code,
                "full_name": student.full_name,
                "roll_number": student.roll_number,
                "email": student.user.email,
                "branch": student.branch,
                "year": student.year,
                "cgpa": student.cgpa,
                "graduation_year": student.graduation_year,
                "gender": student.gender,
                "phone": student.phone,
                "address": student.address,
                "skills": student.skills,
                "github": student.github,
                "linkedin": student.linkedin,
                "portfolio": student.portfolio,
                "resume": ( f"/static/uploads/resumes/{student.resume}" if student.resume else None)
            }
        )


    @staticmethod
    def update_profile(user_id, data):

        student = Student.query.filter_by(user_id=user_id).first()

        if not student:
            return error_response("Student not found.", 404)

        student.full_name = data.get("full_name")
        student.roll_number = data.get("roll_number")
        student.branch = data.get("branch")
        student.year = data.get("year")
        student.cgpa = data.get("cgpa")
        student.graduation_year = data.get("graduation_year")
        student.gender = data.get("gender")
        student.phone = data.get("phone")
        student.address = data.get("address")
        student.skills = data.get("skills")
        student.github = data.get("github")
        student.linkedin = data.get("linkedin")
        student.portfolio = data.get("portfolio")

        db.session.commit()
        cache.delete_memoized(StudentService.get_profile, user_id)

        return success_response(
            "Profile updated successfully."
        )
    
    @staticmethod
    def upload_resume(user_id, file):

        student = Student.query.filter_by(user_id=user_id).first()

        if not student:
            return error_response("Student not found.",404)

        if not file:
            return error_response("No file uploaded.",400)

        filename = secure_filename(file.filename)

        upload_folder = os.path.join(
            current_app.root_path,
            "static",
            "uploads",
            "resumes"
        )

        os.makedirs(upload_folder, exist_ok=True)

        file.save(
            os.path.join(upload_folder, filename)
        )

        student.resume = filename

        db.session.commit()
        cache.delete_memoized(StudentService.get_profile, user_id)

        return success_response("Resume uploaded successfully.")