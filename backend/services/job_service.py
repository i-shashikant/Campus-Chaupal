from datetime import datetime, date

from extensions import db
from models import Job
from utils.response import success_response, error_response
from utils.enums import JobStatus

from extensions import cache

class JobService:

    @staticmethod
    @cache.memoize(timeout=60)
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
                "eligibility_branch": job.eligibility_branch,
                "eligibility_year": job.eligibility_year,
                "deadline": str(job.deadline) if job.deadline else None,
                "company": job.company.company_name if job.company else "",
                "expired": bool(job.deadline and job.deadline < date.today())

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
            eligibility_branch=data.get("eligibility_branch"),
            eligibility_year=data.get("eligibility_year"),
            deadline=deadline,
            status=JobStatus.PENDING.value,
            is_active=False

        )

        db.session.add(job)
        db.session.commit()
        cache.delete_memoized(JobService.get_company_jobs, company_id)
        cache.delete_memoized(JobService.get_all_jobs)

        return success_response(
            "Placement drive submitted for admin approval."
        )

    @staticmethod
    @cache.memoize(timeout=60)
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
                "eligibility_branch": job.eligibility_branch,
                "eligibility_year": job.eligibility_year,
                "deadline": str(job.deadline) if job.deadline else None,
                "status": job.status,
                "reason": job.reason,
                "is_active": job.is_active,
                "applicant_count": len(job.applications)

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
        job.eligibility_branch = data.get(
            "eligibility_branch",
            job.eligibility_branch
        )
        job.eligibility_year = data.get(
            "eligibility_year",
            job.eligibility_year
        )

        if data.get("deadline"):

            job.deadline = datetime.strptime(
                data["deadline"],
                "%Y-%m-%d"
            ).date()

        if job.status == JobStatus.APPROVED.value:
            job.status = JobStatus.PENDING.value
            job.is_active = False

        db.session.commit()
        cache.delete_memoized(JobService.get_company_jobs, company_id)
        cache.delete_memoized(JobService.get_all_jobs)

        return success_response(
            "Job updated successfully. Re-submitted for admin approval."
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
        cache.delete_memoized(JobService.get_company_jobs, company_id)
        cache.delete_memoized(JobService.get_all_jobs)

        return success_response(
            "Job deleted successfully."
        )

    @staticmethod
    def approve_job(job_id):

        job = db.session.get(Job, job_id)

        if not job:
            return error_response("Job not found.", 404)

        job.status = JobStatus.APPROVED.value
        job.is_active = True
        job.reason = None

        db.session.commit()
        cache.delete_memoized(
            JobService.get_company_jobs,
            job.company_id
        )

        cache.delete_memoized(
            JobService.get_all_jobs
        )

        return success_response("Placement drive approved successfully.")

    @staticmethod
    def reject_job(job_id, reason=None):

        job = db.session.get(Job, job_id)

        if not job:
            return error_response("Job not found.", 404)

        job.status = JobStatus.REJECTED.value
        job.is_active = False
        job.reason = reason

        db.session.commit()
        cache.delete_memoized(
            JobService.get_company_jobs,
            job.company_id
        )

        cache.delete_memoized(
            JobService.get_all_jobs
        )

        return success_response("Placement drive rejected.")

    @staticmethod
    def close_job(company_id, job_id):

        job = Job.query.filter_by(
            id=job_id,
            company_id=company_id
        ).first()

        if job is None:
            return error_response("Placement drive not found.", 404)

        job.status = JobStatus.CLOSED.value
        job.is_active = False

        db.session.commit()

        cache.delete_memoized(JobService.get_company_jobs, company_id)
        cache.delete_memoized(JobService.get_all_jobs)

        return success_response(
            "Placement drive closed.",
            {
                "id": job.id,
                "status": job.status,
                "is_active": job.is_active
            }
    )