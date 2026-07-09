from extensions import db
from datetime import datetime
from utils.enums import StudentStatus, Gender

class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    student_code = db.Column(db.String(20), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, unique=True)
    full_name = db.Column(db.String(120), nullable=False)
    roll_number = db.Column(db.String(20), unique=True, nullable=False)
    branch = db.Column(db.String(100))
    cgpa = db.Column(db.Float)
    graduation_year = db.Column(db.Integer)
    gender = db.Column(db.String(30), default=Gender.PREFER_NOT_TO_SAY.value)
    phone = db.Column(db.String(15))
    linkedin = db.Column(db.String(255))
    github = db.Column(db.String(255))
    portfolio = db.Column(db.String(255)) 
    resume = db.Column(db.String(255))
    skills = db.Column(db.Text)
    status = db.Column(db.String(20), default=StudentStatus.ACTIVE.value)
    profile_completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime)
    updated_at = db.Column(db.DateTime, default=datetime, onupdate=datetime)
    user = db.relationship("User", back_populates="student")