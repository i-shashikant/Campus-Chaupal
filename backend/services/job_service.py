from models import Job
from extensions import db
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