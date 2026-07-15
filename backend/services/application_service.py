from extensions import db
from models import Application, Job, Student
from datetime import date
from utils.enums import JobStatus, StudentStatus
from datetime import datetime
from flask import request
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

        job = db.session.get(Job, job_id)

        if not job:
            return error_response("Job not found.", 404)

        eligible, message = ApplicationService.is_eligible(student, job)

        if not eligible:
            return error_response(message, 400)

        exists = Application.query.filter_by(
            student_id=student_id,
            job_id=job_id
        ).first()

        if exists:
            return error_response("Already applied.", 400)

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
                    str(app.applied_at),

                "interview_date": (
                    app.interview_date.strftime("%d %b %Y")
                    if app.interview_date else None
                ),

                "interview_time": (
                    app.interview_time.strftime("%I:%M %p")
                    if app.interview_time else None
                ),

                "interview_mode": app.interview_mode,
                "interview_link": app.interview_link,

                        }),
                    

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

                "applied_at": app.applied_at.strftime("%d %b %Y"),
                "interview_date": app.interview_date.strftime("%d %b %Y") if app.interview_date else None,

                "interview_time":
                    app.interview_time.strftime("%I:%M %p")
                    if app.interview_time else None,

                "interview_mode":
                    app.interview_mode,

                "interview_link":
                    app.interview_link,

               "resume": (
    f"{request.host_url}static/uploads/resumes/{app.student.resume}"
    if app.student.resume else None
),

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
    
    @staticmethod
    def is_eligible(student, job):

        if student.status == StudentStatus.BLACKLISTED.value:
            return False, "Your account has been blacklisted."

        if job.status != JobStatus.APPROVED.value or not job.is_active:
            return False, "This placement drive is not open."

        if job.deadline and job.deadline < date.today():
            return False, "Application deadline has passed."

        if (
            job.eligibility_cgpa
            and (
                student.cgpa is None
                or student.cgpa < job.eligibility_cgpa
            )
        ):
            return False, "Minimum CGPA requirement not met."

        if job.eligibility_branch:

            allowed = [
                b.strip().lower()
                for b in job.eligibility_branch.split(",")
                if b.strip()
            ]

            if (student.branch or "").lower() not in allowed:
                return False, "Branch not eligible."

        if (
            job.eligibility_year
            and student.graduation_year
            and str(student.graduation_year)
            != str(job.eligibility_year)
        ):
            return False, "Graduation year not eligible."

        return True, ""
    


    @staticmethod
    def schedule_interview(application_id, data):

        application = db.session.get(Application, application_id)

        if not application:
            return error_response("Application not found.", 404)

        application.interview_date = datetime.strptime(
            data["interview_date"],
            "%Y-%m-%d"
        ).date()

        application.interview_time = datetime.strptime(
            data["interview_time"],
            "%H:%M"
        ).time()

        application.interview_mode = data.get("interview_mode")
        application.interview_link = data.get("interview_link")

        application.status = "Interview Scheduled"

        db.session.commit()

        return success_response(
            "Interview scheduled successfully."
        )