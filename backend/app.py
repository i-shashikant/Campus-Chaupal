from flask import Flask
from flask_cors import CORS
from flask_security import SQLAlchemyUserDatastore
from config import Config
from extensions import db, migrate, security, mail
from models import Role, User, Student, Company 
from api.auth import auth_bp
from api.student.routes import student_bp
from utils.response import error_response


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore, register_blueprint=False)

    @security.unauthn_handler
    def handle_unauthenticated(mechanisms, headers=None):
        return error_response("Authentication required.", status_code=401)

    @security.unauthz_handler
    def handle_unauthorized(func, params):
        return error_response("You don't have permission to do that.", status_code=403)

    app.register_blueprint(auth_bp)
    app.register_blueprint(student_bp)

    CORS(app)

    @app.route("/")
    def home():
        return {"message": "Placement Portal Backend Running 🚀"}    
    
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)