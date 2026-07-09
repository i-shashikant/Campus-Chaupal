import re


def validate_email(email):
    if not email:
        return False, "Email is required."

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(pattern, email):
        return False, "Invalid email address."

    return True, ""


def validate_password(password):
    if not password:
        return False, "Password is required."

    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    if len(password) > 32:
        return False, "Password cannot exceed 32 characters."

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."

    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."

    return True, ""