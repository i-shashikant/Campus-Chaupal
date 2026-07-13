from enum import Enum


class Role(Enum):
    ADMIN = "admin"
    STUDENT = "student"
    COMPANY = "company"


class UserStatus(Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    SUSPENDED = "Suspended"


class StudentStatus(Enum):
    ACTIVE = "Active"
    BLACKLISTED = "Blacklisted"


class CompanyStatus(Enum):
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    BLACKLISTED = "Blacklisted"


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"
    PREFER_NOT_TO_SAY = "Prefer not to say"

