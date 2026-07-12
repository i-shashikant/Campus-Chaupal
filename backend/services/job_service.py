from models import Job
from extensions import db
from utils.response import success_response, error_response
from datetime import datetime


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