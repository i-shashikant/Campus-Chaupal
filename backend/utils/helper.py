from models.student import Student
from models.company import Company


def generate_student_code():

    last_student = Student.query.order_by(Student.id.desc()).first()

    if not last_student:
        return "STU00001"

    next_id = last_student.id + 1

    return f"STU{next_id:05d}"


def generate_company_code():

    last_company = Company.query.order_by(Company.id.desc()).first()

    if not last_company:
        return "COM00001"

    next_id = last_company.id + 1

    return f"COM{next_id:05d}"