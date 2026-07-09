from flask import Blueprint
from . import routes

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/auth"
)

