"""
Celery entrypoint for the Placement Portal.

Run the worker (handles async + scheduled tasks):
    celery -A celery_worker.celery worker --loglevel=info --pool=solo   (Windows)
    celery -A celery_worker.celery worker --loglevel=info               (Mac/Linux)

Run the beat scheduler (fires the daily reminder + monthly report on schedule),
in a SEPARATE terminal:
    celery -A celery_worker.celery beat --loglevel=info

Both need Redis running locally on the default port (redis-server).
"""

from celery import Celery
from celery.schedules import crontab

from app import create_app


def make_celery(flask_app):
    celery_app = Celery(
        flask_app.import_name,
        broker=flask_app.config["CELERY_BROKER_URL"],
        backend=flask_app.config["CELERY_RESULT_BACKEND"],
    )
    celery_app.conf.update(flask_app.config)

    class ContextTask(celery_app.Task):
        """Make sure every task runs inside a Flask app context,
        so db.session / models / mail all work normally."""

        def __call__(self, *args, **kwargs):
            with flask_app.app_context():
                return self.run(*args, **kwargs)

    celery_app.Task = ContextTask
    return celery_app


flask_app = create_app()
celery = make_celery(flask_app)

# Register scheduled (periodic) jobs
celery.conf.beat_schedule = {
    "daily-deadline-reminders": {
        "task": "tasks.reminder_tasks.send_daily_deadline_reminders",
        "schedule": crontab(hour=8, minute=0),   # every day at 08:00
    },
    "monthly-activity-report": {
        "task": "tasks.report_tasks.send_monthly_activity_report",
        "schedule": crontab(hour=6, minute=0, day_of_month=1),  # 1st of month, 06:00
    },
}
celery.conf.timezone = flask_app.config.get("CELERY_TIMEZONE", "UTC")

# Import task modules so Celery registers them
from tasks import reminder_tasks, report_tasks, export_tasks  # noqa: E402,F401