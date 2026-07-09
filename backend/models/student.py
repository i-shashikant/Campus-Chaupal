from extensions import db


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, unique=True)
    roll_number = db.Column(db.String(20), unique=True, nullable=False)
    branch = db.Column(db.String(100))
    cgpa = db.Column(db.Float)
    graduation_year = db.Column(db.Integer)
    phone = db.Column(db.String(15))
    resume = db.Column(db.String(255))
    skills = db.Column(db.Text)
    user = db.relationship("User", back_populates="student")