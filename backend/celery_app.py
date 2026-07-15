from celery import Celery
from app import create_app
from celery.schedules import crontab
import tasks.reminders
import tasks.report_tasks


flask_app = create_app()

celery = Celery(
    flask_app.import_name,
    broker=flask_app.config["CELERY_BROKER_URL"],
    backend=flask_app.config["CELERY_RESULT_BACKEND"],
)

celery.conf.update(
    timezone="Asia/Kolkata",
    enable_utc=False,
)


class ContextTask(celery.Task):
    def __call__(self, *args, **kwargs):
        with flask_app.app_context():
            return self.run(*args, **kwargs)


celery.Task = ContextTask

celery.conf.beat_schedule = {
    "daily-reminder": {
        "task": "tasks.reminders.daily_reminder",
        "schedule": crontab(hour=9, minute=0),
    },

    "monthly-report": {
        "task": "tasks.report_tasks.monthly_report",
        "schedule": crontab(hour=9, minute=0, day_of_month=1),
    },
}

