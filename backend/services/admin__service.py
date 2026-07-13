from models import Student, Company, Job, Application
from utils.enums import CompanyStatus
from utils.response import success_response


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