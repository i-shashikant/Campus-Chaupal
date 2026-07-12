import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "placement_secret_key"

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "instance", "placement.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

  
    SECURITY_PASSWORD_SALT = "placement-portal-salt-change-me"
    SECURITY_PASSWORD_HASH = "bcrypt"

    
    SECURITY_REGISTERABLE = False
    SECURITY_RECOVERABLE = False
    SECURITY_CONFIRMABLE = False
    SECURITY_CHANGEABLE = False


    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"
    SECURITY_TOKEN_MAX_AGE = 60 * 60 * 24  # 24 hrs

 
    WTF_CSRF_ENABLED = False
    SECURITY_CSRF_PROTECT_MECHANISMS = []


    MAIL_SERVER = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT = int(os.environ.get("MAIL_PORT", 587))
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME", "")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD", "")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_USERNAME", "placements@campus.edu")

    REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/0")
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_URL = REDIS_URL
    CACHE_DEFAULT_TIMEOUT = 120

    CELERY_BROKER_URL = REDIS_URL
    CELERY_RESULT_BACKEND = REDIS_URL

    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")