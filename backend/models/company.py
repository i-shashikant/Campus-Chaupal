from extensions import db


class Company(db.Model):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, unique=True)
    company_name = db.Column(db.String(150), nullable=False)
    website = db.Column(db.String(255))
    location = db.Column(db.String(150))
    hr_name = db.Column(db.String(100))
    hr_email = db.Column(db.String(120))
    phone = db.Column(db.String(15))
    description = db.Column(db.Text)
    user = db.relationship("User", back_populates="company")
    jobs = db.relationship("Job", back_populates="company", cascade="all, delete-orphan")