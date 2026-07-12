from datetime import datetime
from extensions import db
from flask_security import UserMixin
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from models.role import roles_users
from extensions import db
from utils.enums import Role, UserStatus

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=True)
    password = db.Column(db.String(255), nullable=False)
    fs_uniquifier = db.Column(db.String(64), unique=True, nullable=False, default=lambda: uuid.uuid4().hex)
    role = db.Column(db.String(20), nullable=False)

    status = db.Column(db.String(20), default=UserStatus.ACTIVE.value)
    active = db.Column(db.Boolean, default=True)
    is_email_verified = db.Column(db.Boolean, default=False)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = db.Column(db.DateTime)

    roles = db.relationship("Role", secondary=roles_users, backref=db.backref("users", lazy="dynamic"))


    student = db.relationship("Student", back_populates="user", uselist=False, cascade="all, delete-orphan")
    company = db.relationship("Company", back_populates="user", uselist=False, cascade="all, delete-orphan")

    def has_role_name(self, name: str) -> bool:
        """convenience check against the plain `role` string, not the RBAC table"""
        return self.role == name

    def __repr__(self):
        return f"<User {self.email}>"
