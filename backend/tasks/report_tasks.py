# from datetime import date, timedelta
# from flask import current_app
# from flask_mail import Message

# from celery_worker import celery
# from extensions import mail
# from models import Job, Application
# from utils.enums import JobStatus


# @celery.task(name="tasks.report_tasks.send_monthly_activity_report")
# def send_monthly_activity_report():
#     first_of_this_month = date.today().replace(day=1)
#     last_day_prev_month = first_of_this_month - timedelta(days=1)
#     first_day_prev_month = last_day_prev_month.replace(day=1)

#     drives = Job.query.filter(
#         Job.created_at >= first_day_prev_month,
#         Job.created_at <= last_day_prev_month
#     ).all()

#     applications = Application.query.filter(
#         Application.applied_at >= first_day_prev_month,
#         Application.applied_at <= last_day_prev_month
#     ).all()

#     selected_count = sum(1 for a in applications if a.status == "Selected")
#     approved_drives = sum(1 for d in drives if d.status == JobStatus.APPROVED.value)

#     rows = ""
#     for job in drives:
#         rows += (
#             f"<tr><td>{job.title}</td><td>{job.company.company_name}</td>"
#             f"<td>{job.status}</td><td>{len(job.applications)}</td></tr>"
#         )

#     if not rows:
#         rows = "<tr><td colspan='4'>No drives were created this month</td></tr>"

#     html = f"""
#     <html>
#     <body style="font-family: Arial, sans-serif;">
#         <h2>Monthly Placement Activity Report</h2>
#         <p>Period: {first_day_prev_month.strftime('%d %b %Y')} to {last_day_prev_month.strftime('%d %b %Y')}</p>
#         <ul>
#             <li>Total drives created: {len(drives)}</li>
#             <li>Drives approved by admin: {approved_drives}</li>
#             <li>Total student applications: {len(applications)}</li>
#             <li>Students selected: {selected_count}</li>
#         </ul>
#         <h3>Drive wise breakdown</h3>
#         <table border="1" cellpadding="6" cellspacing="0">
#             <tr><th>Job Title</th><th>Company</th><th>Status</th><th>Applications</th></tr>
#             {rows}
#         </table>
#     </body>
#     </html>
#     """

#     recipient = current_app.config.get("ADMIN_REPORT_EMAIL")

#     msg = Message(
#         subject=f"Placement Activity Report - {first_day_prev_month.strftime('%B %Y')}",
#         recipients=[recipient],
#         html=html
#     )

#     mail.send(msg)

#     return f"report sent to {recipient} for {len(drives)} drives"