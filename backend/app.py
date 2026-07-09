from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db, jwt, migrate
from models import User, Student, Company 
from api.auth import auth_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    @app.route("/")
    def home():
        return {
            "message": "Placement Portal Backend Running 🚀"
        }

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)