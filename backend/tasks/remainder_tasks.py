from datetime import date, timedelta
import requests
from flask import current_app
from flask_mail import Message

from celery_worker import celery
from extensions import mail
from models import Job, Student, Application
from utils.enums import JobStatus, StudentStatus


@celery.task(name="tasks.reminder_tasks.send_daily_deadline_reminders")
def send_daily_deadline_reminders():
    today = date.today()
    upcoming = today + timedelta(days=2)

    jobs = Job.query.filter(
        Job.status == JobStatus.APPROVED.value,
        Job.is_active == True,
        Job.deadline.isnot(None),
        Job.deadline >= today,
        Job.deadline <= upcoming
    ).all()

    if not jobs:
        return "no drives closing in next 2 days"

    students = Student.query.filter_by(status=StudentStatus.ACTIVE.value).all()
    sent_count = 0

    for student in students:
        matched_jobs = []

        for job in jobs:
            if job.eligibility_cgpa and student.cgpa and student.cgpa < job.eligibility_cgpa:
                continue

            if job.eligibility_year and student.year and student.year != job.eligibility_year:
                continue

            if job.eligibility_branch and student.branch:
                allowed = [b.strip().lower() for b in job.eligibility_branch.split(",")]
                if student.branch.lower() not in allowed:
                    continue

            already_applied = Application.query.filter_by(
                student_id=student.id, job_id=job.id
            ).first()

            if already_applied:
                continue

            matched_jobs.append(job)

        if not matched_jobs or not student.user:
            continue

        lines = []
        for job in matched_jobs:
            deadline_str = job.deadline.strftime("%d %b %Y")
            lines.append(f"- {job.title} at {job.company.company_name}, deadline {deadline_str}")

        body = "Hi " + (student.full_name or "there") + ",\n\n"
        body += "These placement drives you are eligible for are closing in the next 2 days:\n\n"
        body += "\n".join(lines)
        body += "\n\nPlease log in to the placement portal and apply before the deadline.\n"

        try:
            msg = Message(
                subject="Placement Drive Deadline Reminder",
                recipients=[student.user.email],
                body=body
            )
            mail.send(msg)
            sent_count += 1
        except Exception as e:
            print("could not send reminder to", student.user.email, "-", e)

    notify_admin_on_gchat(len(jobs), sent_count)

    return f"reminders sent to {sent_count} students across {len(jobs)} drives"


def notify_admin_on_gchat(drive_count, student_count):
    webhook_url = current_app.config.get("GCHAT_WEBHOOK_URL")

    if not webhook_url:
        return

    text = (
        f"Daily reminder job finished. {drive_count} drives closing in the next 2 days, "
        f"reminders sent to {student_count} students."
    )

    try:
        requests.post(webhook_url, json={"text": text}, timeout=5)
    except Exception as e:
        print("gchat webhook call failed -", e)