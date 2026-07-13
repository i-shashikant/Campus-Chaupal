from datetime import datetime
from extensions import db
from utils.enums import JobStatus

class Job(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)

    company_id = db.Column(
        db.Integer,
        db.ForeignKey("companies.id"),
        nullable=False
    )

    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(120))
    job_type = db.Column(db.String(50))
    salary_package = db.Column(db.String(50))

    eligibility_cgpa = db.Column(db.Float)
    eligibility_branch = db.Column(db.String(255))
    eligibility_year = db.Column(db.Integer)
    deadline = db.Column(db.Date)

    status = db.Column(db.String(20), default=JobStatus.PENDING.value)
    is_active = db.Column(db.Boolean, default=True)
    reason = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    company = db.relationship(
        "Company",
        back_populates="jobs"
    )