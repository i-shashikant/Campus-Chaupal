from extensions import db
from datetime import datetime
from utils.enums import CompanyStatus


class Company(db.Model):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)
    company_code = db.Column(db.String(50), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, unique=True)

    company_name = db.Column(db.String(150), nullable=False)
    website = db.Column(db.String(255))
    location = db.Column(db.String(150))
    industry = db.Column(db.String(100))
    hr_name = db.Column(db.String(100))
    hr_email = db.Column(db.String(120))
    phone = db.Column(db.String(15))
    description = db.Column(db.Text)
    address = db.Column(db.String(255))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(100))
    logo = db.Column(db.String(255))
    status = db.Column(db.String(20), default=CompanyStatus.PENDING.value)
    profile_completed = db.Column(db.Boolean, default=False)
    verified = db.Column(db.Boolean, default=False)
    reason = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime)
    updated_at = db.Column(db.DateTime, default=datetime, onupdate=datetime)
    user = db.relationship("User", back_populates="company")
    jobs = db.relationship("Job", back_populates="company", cascade="all, delete-orphan")