from extensions import db
from models import Application, Job, Student
from datetime import date
from utils.enums import JobStatus, StudentStatus


from utils.response import (
    success_response,
    error_response
)


class ApplicationService:

    @staticmethod
    def apply(student_id, job_id):

        student = db.session.get(Student, student_id)

        if not student:
            return error_response("Student not found.", 404)

        if student.status == StudentStatus.BLACKLISTED.value:
            return error_response(
                "Your account has been blacklisted. Contact the placement cell.",
                403
            )

        job = db.session.get(Job, job_id)

        if not job:
            return error_response("Job not found.", 404)

        if job.status != JobStatus.APPROVED.value or not job.is_active:
            return error_response(
                "This placement drive is not open for applications.",
                400
            )

        if job.deadline and job.deadline < date.today():
            return error_response(
                "Application deadline has passed.",
                400
            )

        if job.eligibility_cgpa and (
            student.cgpa is None or student.cgpa < job.eligibility_cgpa
        ):
            return error_response(
                "You do not meet the minimum CGPA requirement.",
                400
            )

        if job.eligibility_branch:
            allowed = [
                b.strip().lower()
                for b in job.eligibility_branch.split(",")
                if b.strip()
            ]
            if allowed and (student.branch or "").lower() not in allowed:
                return error_response(
                    "You are not eligible for this drive based on branch.",
                    400
                )

        if job.eligibility_year and student.graduation_year and (
            str(student.graduation_year) != str(job.eligibility_year)
        ):
            return error_response(
                "You are not eligible for this drive based on graduation year.",
                400
            )

        exists = Application.query.filter_by(
            student_id=student_id,
            job_id=job_id
        ).first()

        if exists:

            return error_response(
                "Already applied.",
                400
            )

        application = Application(

            student_id=student_id,
            job_id=job_id

        )

        db.session.add(application)

        db.session.commit()

        return success_response(
            "Application submitted successfully."
        )

    @staticmethod
    def student_applications(student_id):

        apps = Application.query.filter_by(
            student_id=student_id
        ).all()

        data = []

        for app in apps:

            data.append({

                "id": app.id,

                "company":
                    app.job.company.company_name,

                "title":
                    app.job.title,

                "status":
                    app.status,

                "applied_at":
                    str(app.applied_at)

            })

        return success_response(
            "Applications fetched.",
            data
        )

    @staticmethod
    def company_applications(company_id):

        apps = Application.query.join(Job).filter(
            Job.company_id == company_id
        ).all()

        data = []

        for app in apps:

            data.append({

                "id": app.id,

                "student":

                    app.student.full_name,

                "job":

                    app.job.title,

                "status":

                    app.status,

                "applied_at": app.applied_at.strftime("%d %b %Y")

            })

        return success_response(
            "Applications fetched.",
            data
        )

    @staticmethod
    def update_application_status(company_id, application_id, data):

        application = (
            Application.query
            .join(Job)
            .filter(
                Application.id == application_id,
                Job.company_id == company_id
            )
            .first()
        )

        if not application:
            return error_response(
                "Application not found.",
                404
            )

        allowed_status = [
            "Applied",
            "Shortlisted",
            "Selected",
            "Rejected"
        ]

        status = data.get("status")

        if status not in allowed_status:
            return error_response(
                "Invalid status.",
                400
            )

        application.status = status

        db.session.commit()

        return success_response(
            "Application status updated successfully."
        )