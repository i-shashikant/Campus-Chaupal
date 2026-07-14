from datetime import datetime
from extensions import db


class Application(db.Model):

    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )

    job_id = db.Column(
        db.Integer,
        db.ForeignKey("jobs.id"),
        nullable=False
    )

    status = db.Column(
        db.String(30),
        default="Applied"
    )

    applied_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    student = db.relationship(
        "Student",
        backref="applications"
    )

    job = db.relationship(
        "Job",
        backref="applications"
    )
    interview_date = db.Column(db.Date)
    interview_time = db.Column(db.Time)
    interview_mode = db.Column(db.String(50))
    interview_link = db.Column(db.String(255))