from extensions import db, security
from models import User, Student, Company

from utils.response import success_response, error_response


class CompanyService:

    @staticmethod
    def get_profile(user_id):

        company = Company.query.filter_by(user_id=user_id).first()

        if not company:
            return error_response("Company not found.", 404)

        return success_response(
            "Profile fetched.",
            {
                "company_code": company.company_code,
                "company_name": company.company_name,
                "website": company.website,
                "location": company.location,
                "industry": company.industry,
                "hr_name": company.hr_name,
                "hr_email": company.hr_email,
                "phone": company.phone,
                "description": company.description,
                "address": company.address,
                "city": company.city,
                "state": company.state,
                "country": company.country,
                "status": company.status,
                "verified": company.verified,
                "profile_completed": company.profile_completed,
            }
        )


    @staticmethod
    def update_profile(user_id, data):

        company = Company.query.filter_by(user_id=user_id).first()

        if not company:
            return error_response("Company not found.", 404)

        company.company_name = data.get("company_name", company.company_name)
        company.website = data.get("website", company.website)
        company.location = data.get("location", company.location)
        company.industry = data.get("industry", company.industry)
        company.hr_name = data.get("hr_name", company.hr_name)
        company.hr_email = data.get("hr_email", company.hr_email)
        company.phone = data.get("phone", company.phone)
        company.description = data.get("description", company.description)
        company.address = data.get("address", company.address)
        company.city = data.get("city", company.city)
        company.state = data.get("state", company.state)
        company.country = data.get("country", company.country)

        company.profile_completed = True

        db.session.commit()

        return success_response("Profile updated successfully.")