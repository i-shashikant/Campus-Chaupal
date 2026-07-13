from datetime import datetime

from extensions import db
from models import Job
from utils.response import success_response, error_response


class JobService:

    @staticmethod
    def get_all_jobs():

        jobs = Job.query.filter_by(is_active=True).all()

        data = []

        for job in jobs:

            data.append({

                "id": job.id,
                "title": job.title,
                "description": job.description,
                "location": job.location,
                "job_type": job.job_type,
                "salary_package": job.salary_package,
                "eligibility_cgpa": job.eligibility_cgpa,
                "deadline": str(job.deadline) if job.deadline else None,
                "company": job.company.company_name if job.company else ""

            })

        return success_response(
            "Jobs fetched successfully.",
            data
        )

    @staticmethod
    def create_job(company_id, data):

        deadline = None

        if data.get("deadline"):

            deadline = datetime.strptime(
                data["deadline"],
                "%Y-%m-%d"
            ).date()

        job = Job(

            company_id=company_id,
            title=data.get("title"),
            description=data.get("description"),
            location=data.get("location"),
            salary_package=data.get("salary_package"),
            job_type=data.get("job_type"),
            eligibility_cgpa=data.get("eligibility_cgpa"),
            deadline=deadline

        )

        db.session.add(job)
        db.session.commit()

        return success_response(
            "Job created successfully."
        )

    @staticmethod
    def get_company_jobs(company_id):

        jobs = Job.query.filter_by(company_id=company_id).all()

        data = []

        for job in jobs:

            data.append({

                "id": job.id,
                "title": job.title,
                "description": job.description,
                "location": job.location,
                "job_type": job.job_type,
                "salary_package": job.salary_package,
                "eligibility_cgpa": job.eligibility_cgpa,
                "deadline": str(job.deadline) if job.deadline else None,
                "is_active": job.is_active

            })

        return success_response(
            "Jobs fetched successfully.",
            data
        )

    @staticmethod
    def update_job(company_id, job_id, data):

        job = Job.query.filter_by(
            id=job_id,
            company_id=company_id
        ).first()

        if not job:

            return error_response(
                "Job not found.",
                404
            )

        job.title = data.get("title", job.title)
        job.description = data.get("description", job.description)
        job.location = data.get("location", job.location)
        job.job_type = data.get("job_type", job.job_type)
        job.salary_package = data.get("salary_package", job.salary_package)
        job.eligibility_cgpa = data.get(
            "eligibility_cgpa",
            job.eligibility_cgpa
        )

        if data.get("deadline"):

            job.deadline = datetime.strptime(
                data["deadline"],
                "%Y-%m-%d"
            ).date()

        db.session.commit()

        return success_response(
            "Job updated successfully."
        )

    @staticmethod
    def delete_job(company_id, job_id):

        job = Job.query.filter_by(
            id=job_id,
            company_id=company_id
        ).first()

        if not job:

            return error_response(
                "Job not found.",
                404
            )

        db.session.delete(job)
        db.session.commit()

        return success_response(
            "Job deleted successfully."
        )