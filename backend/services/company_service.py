from extensions import db, security
from models import User, Student, Company
import os
from werkzeug.utils import secure_filename
from flask import current_app
from utils.response import success_response, error_response
from extensions import cache

class CompanyService:

    @staticmethod
    @cache.memoize(timeout=60)
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
                "logo": f"/static/uploads/company/{company.logo}"
            },
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
        cache.delete_memoized(CompanyService.get_profile, user_id)

        return success_response("Profile updated successfully.")
    
    @staticmethod
    def upload_logo(user_id, files):

        company = Company.query.filter_by(
            user_id=user_id
        ).first()

        if not company:
            return error_response(
                "Company not found.",
                404
            )

        file = files.get("logo")

        if not file:
            return error_response(
                "No logo selected.",
                400
            )

        filename = secure_filename(file.filename)

        upload_folder = os.path.join(
            current_app.root_path,
            "static",
            "uploads",
            "company"
        )

        os.makedirs(upload_folder, exist_ok=True)

        filepath = os.path.join(
            upload_folder,
            filename
        )

        file.save(filepath)

        company.logo = filename

        db.session.commit()
        cache.delete_memoized(CompanyService.get_profile, user_id)

        return success_response(
            "Logo uploaded successfully.",
            {
                "logo":
                f"/static/uploads/company/{filename}"
            }
        )