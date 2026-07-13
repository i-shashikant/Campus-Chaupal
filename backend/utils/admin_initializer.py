from extensions import db, security
from flask_security import hash_password
from models import User
from utils.enums import Role


def initialize_admin():

    admin = User.query.filter_by(
        email="admin@campuschaupal.com"
    ).first()

    if admin:
        return

    admin_role = security.datastore.find_or_create_role(
        name=Role.ADMIN.value,
        description="Administrator"
    )

    admin = security.datastore.create_user(
        email="admin@campuschaupal.com",
        password=hash_password("Admin@123"),
        role=Role.ADMIN.value,
        active=True,
    )

    security.datastore.add_role_to_user(
        admin,
        admin_role
    )

    db.session.commit()

    print("✅ Default Admin Created") 