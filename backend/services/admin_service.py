from models import Student, Company, Job, Application
from utils.enums import CompanyStatus
from utils.response import success_response, error_response
from extensions import db


class AdminService:

    @staticmethod
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
            "active_jobs": Job.query.filter_by(
                is_active=True
            ).count(),
            "applications": Application.query.count(),
        }

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