from datetime import date

from models import Student, Company, Job, Application, User
from utils.enums import CompanyStatus, StudentStatus, JobStatus
from utils.response import success_response, error_response
from extensions import db
from sqlalchemy import func
from models import Student, Company, Job, Application
from extensions import cache

class AdminService:
    
    @staticmethod
    @cache.cached(timeout=60)
    def dashboard():

        data = {
            "students": Student.query.count(),
            "companies": Company.query.count(),
            "pending_companies": Company.query.filter_by(
                status=CompanyStatus.PENDING.value
            ).count(),
            "approved_companies": Company.query.filter_by(
                status=CompanyStatus.APPROVED.value
            ).count(),
            "jobs": Job.query.count(),
            "pending_jobs": Job.query.filter_by(
                status=JobStatus.PENDING.value
            ).count(),
            "active_jobs": Job.query.filter_by(
                is_active=True
            ).count(),
            "applications": Application.query.count(),
        }

        # Selected Students

        selected = Application.query.filter_by(
            status="Selected"
        ).count()

        # Placement Rate

        applications = data["applications"]

        placement_rate = round(
            (selected / applications) * 100,
            2
        ) if applications else 0

        # Most Active Company

        company_stats = (
            db.session.query(
                Company.company_name,
                func.count(Job.id).label("jobs")
            )
            .join(Job)
            .group_by(Company.id)
            .order_by(func.count(Job.id).desc())
            .first()
        )

        most_active_company = (
            company_stats[0]
            if company_stats else "N/A"
        )

        most_active_company_jobs = (
            company_stats[1]
            if company_stats else 0
        )

        # Average CGPA

        average_cgpa = db.session.query(
            func.avg(Student.cgpa)
        ).scalar()

        average_cgpa = round(
            average_cgpa or 0,
            2
        )

        # Add new statistics

        data["selected"] = selected
        data["placement_rate"] = placement_rate
        data["most_active_company"] = most_active_company
        data["most_active_company_jobs"] = most_active_company_jobs
        data["average_cgpa"] = average_cgpa

        return success_response(
            "Dashboard fetched successfully.",
            data
        )

    @staticmethod
    def pending_companies():

        companies = Company.query.filter_by(
            status=CompanyStatus.PENDING.value
        ).all()

        data = []

        for company in companies:

            data.append({
                "id": company.id,
                "company_name": company.company_name,
                "company_code": company.company_code,
                "email": company.user.email,
                "location": company.location,
                "industry": company.industry,
                "status": company.status,
                "created_at": company.created_at.strftime("%d %b %Y")
            })

        return success_response(
            "Pending companies fetched successfully.",
            data
        )

    @staticmethod
    def get_companies():

        companies = Company.query.order_by(
            Company.created_at.desc()
        ).all()

        data = []

        for company in companies:

            data.append({
                "id": company.id,
                "company_name": company.company_name,
                "company_code": company.company_code,
                "email": company.user.email,
                "location": company.location,
                "industry": company.industry,
                "status": company.status,
                "created_at": company.created_at.strftime("%d %b %Y")
            })

        return success_response(
            "Companies fetched successfully.",
            data
        )

    @staticmethod
    def approve_company(company_id):

        company = db.session.get(Company, company_id)

        if not company:
            return error_response("Company not found.", 404)

        if company.status == CompanyStatus.APPROVED.value:
            return error_response("Company is already approved.")

        company.status = CompanyStatus.APPROVED.value
        company.verified = True

        db.session.commit()

        return success_response("Company approved successfully.")

    @staticmethod
    def reject_company(company_id):

        company = db.session.get(Company, company_id)

        if not company:
            return error_response("Company not found.", 404)

        if company.status == CompanyStatus.REJECTED.value:
            return error_response("Company is already rejected.")

        company.status = CompanyStatus.REJECTED.value
        company.verified = False

        db.session.commit()

        return success_response("Company rejected successfully.")

    @staticmethod
    def blacklist_company(company_id):

        company = db.session.get(Company, company_id)

        if not company:
            return error_response("Company not found.", 404)

        company.status = CompanyStatus.BLACKLISTED.value
        company.verified = False

        for job in company.jobs:
            job.is_active = False

        db.session.commit()

        return success_response("Company blacklisted successfully.")

    @staticmethod
    def unblock_company(company_id):

        company = db.session.get(Company, company_id)

        if not company:
            return error_response("Company not found.", 404)

        company.status = CompanyStatus.APPROVED.value
        company.verified = True

        db.session.commit()

        return success_response("Company unblocked successfully.")

    @staticmethod
    def get_users():

        users = User.query.filter_by(role="student") \
        .order_by(User.created_at.desc()) \
        .all()

        data = []

        for user in users:

            data.append({
                "id": user.id,
                "student_id": user.student.id if user.student else None,
                "name": user.student.full_name if user.student else "-",
                "email": user.email,
                "role": user.role,
                "status": user.student.status if user.student else user.status,
                "active": user.active
            })

        return success_response(
            "Users fetched successfully.",
            data
        )

    @staticmethod
    def blacklist_student(student_id):

        student = db.session.get(Student, student_id)

        if not student:
            return error_response("Student not found.", 404)

        student.status = StudentStatus.BLACKLISTED.value

        db.session.commit()

        return success_response("Student blacklisted successfully.")

    @staticmethod
    def unblock_student(student_id):

        student = db.session.get(Student, student_id)

        if not student:
            return error_response("Student not found.", 404)

        student.status = StudentStatus.ACTIVE.value

        db.session.commit()

        return success_response("Student unblocked successfully.")

    @staticmethod
    def get_jobs():

        jobs = Job.query.order_by(Job.created_at.desc()).all()

        data = []

        for job in jobs:

            data.append({
                "id": job.id,
                "title": job.title,
                "company": job.company.company_name,
                "location": job.location,
                "deadline": job.deadline.strftime("%d %b %Y") if job.deadline else None,
                "expired": bool(job.deadline and job.deadline < date.today()),
                "applications": len(job.applications),
                "status": job.status,
                "active": job.is_active
            })

        return success_response(
            "Jobs fetched successfully.",
            data
        )

    @staticmethod
    def pending_jobs():

        jobs = Job.query.filter_by(
            status=JobStatus.PENDING.value
        ).order_by(Job.created_at.desc()).all()

        data = []

        for job in jobs:

            data.append({
                "id": job.id,
                "title": job.title,
                "company": job.company.company_name,
                "description": job.description,
                "location": job.location,
                "eligibility_cgpa": job.eligibility_cgpa,
                "eligibility_branch": job.eligibility_branch,
                "eligibility_year": job.eligibility_year,
                "deadline": job.deadline.strftime("%d %b %Y") if job.deadline else None,
                "status": job.status
            })

        return success_response(
            "Pending drives fetched successfully.",
            data
        )

    @staticmethod
    def approve_job(job_id):

        from services.job_service import JobService
        return JobService.approve_job(job_id)

    @staticmethod
    def reject_job(job_id, reason=None):

        from services.job_service import JobService
        return JobService.reject_job(job_id, reason)

    @staticmethod
    def get_applications():

        applications = Application.query.order_by(
            Application.applied_at.desc()
        ).all()

        data = []

        for application in applications:

            data.append({
                "id": application.id,
                "student": application.student.full_name,
                "company": application.job.company.company_name,
                "job": application.job.title,
                "status": application.status,
                "applied_at": application.applied_at.strftime("%d %b %Y")
            })

        return success_response(
            "Applications fetched successfully.",
            data
        )