import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "placement_secret_key"
    JWT_SECRET_KEY = "Placement-jwt-secret"

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "instance", "placement.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False