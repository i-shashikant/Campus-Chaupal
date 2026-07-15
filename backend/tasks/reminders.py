from datetime import date, timedelta

from celery import shared_task
from flask_mail import Message

from extensions import mail
from models import Job, Student, Application
from services.application_service import ApplicationService
from utils.enums import JobStatus


@shared_task(name="tasks.reminders.daily_reminder")
def daily_reminder():

    tomorrow = date.today() + timedelta(days=1)

    jobs = Job.query.filter(
        Job.deadline == tomorrow,
        Job.status == JobStatus.APPROVED.value,
        Job.is_active == True
    ).all()

    emails_sent = 0

    for job in jobs:

        students = Student.query.all()

        for student in students:

            already_applied = Application.query.filter_by(
                student_id=student.id,
                job_id=job.id
            ).first()

            if already_applied:
                continue

            eligible, _ = ApplicationService.is_eligible(student, job)

            if not eligible:
                continue

            msg = Message(
                subject=f"Reminder: {job.title} closes tomorrow",
                recipients=[student.user.email]
            )

            msg.body = f"""
Hello {student.full_name},

The placement drive

{job.title}

will close tomorrow.

Company: {job.company.company_name}
Deadline: {job.deadline}

Login to CampusChaupal and apply before the deadline.

Placement Cell
"""

            mail.send(msg)
            emails_sent += 1

    return f"{emails_sent} reminder emails sent."