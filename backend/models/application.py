from extensions import db
from models import Application, Job

from utils.response import (
    success_response,
    error_response
)


class ApplicationService:

    @staticmethod
    def apply(student_id, job_id):

        exists = Application.query.filter_by(
            student_id=student_id,
            job_id=job_id
        ).first()

        if exists:

            return error_response(
                "Already applied.",
                400
            )

        job = Job.query.get(job_id)

        if not job:

            return error_response(
                "Job not found.",
                404
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

                    app.status

            })

        return success_response(
            "Applications fetched.",
            data
        )