# CampusChaupal – Placement Portal
### Bridging the Gap Between Campus and Corporate

CampusChaupal is a full-stack campus placement management portal developed as the **Modern Application Development II (MAD-II)** project. It provides a centralized platform for students, companies, and administrators to manage campus recruitment activities.

---

# Project Overview

CampusChaupal digitizes the campus placement process by enabling:

- Student Registration & Profile Management
- Company Registration & Verification
- Placement Drive Creation
- Job Applications
- Resume Upload
- Interview Scheduling
- Admin Approval Workflow
- Background Email Notifications
- Monthly Placement Reports
- Placement Analytics Dashboard

---

# Technology Stack

## Backend

- Python 3.13
- Flask
- Flask Security
- Flask SQLAlchemy
- Flask Migrate
- Flask Mail
- Flask Caching
- Redis / Memurai
- Celery
- SQLite

---

## Frontend

- Vue 3
- Vite
- Vue Router
- Pinia
- Axios
- Bootstrap 5

---

# Architecture

The project follows a modular layered architecture.

```
Frontend (Vue 3)

        │
        │ REST APIs
        ▼

Flask Blueprints

        │

Service Layer

        │

SQLAlchemy ORM

        │

SQLite Database
```

Background tasks:

```
Frontend
      │
      ▼
Flask API
      │
      ▼
Celery Worker
      │
      ▼
Redis (Broker)
```

---

# Project Structure

```
backend/

│
├── api/
│     ├── admin/
│     ├── application/
│     ├── auth/
│     ├── company/
│     ├── job/
│     └── student/
│
├── models/
│
├── services/
│
├── tasks/
│
├── utils/
│
├── static/
│      └── uploads/
│             ├── company/
│             └── resumes/
│
├── app.py
├── celery_app.py
├── config.py
└── requirements.txt


frontend/

│
├── public/
├── src/
│     ├── assets/
│     ├── components/
│     ├── layouts/
│     ├── pages/
│     ├── router/
│     ├── services/
│     ├── stores/
│     ├── utils/
│     └── views/
│
├── package.json
└── vite.config.js
```

---

# User Roles

## Student

- Register
- Login
- Edit Profile
- Upload Resume
- Browse Jobs
- Apply for Jobs
- View Placement History
- Download Placement History (CSV)
- View Interview Details

---

## Company

- Register
- Login
- Edit Company Profile
- Upload Company Logo
- Create Placement Drive
- Edit Placement Drive
- Close Placement Drive
- Delete Placement Drive
- Review Applications
- Schedule Interviews
- Update Candidate Status

---

## Administrator

- Login
- Dashboard Analytics
- Approve Companies
- Reject Companies
- Blacklist Companies
- Activate Companies
- View Students
- Blacklist Students
- Activate Students
- Approve Placement Drives
- Reject Placement Drives

---

# Major Features

## Authentication

- Role Based Authentication
- Flask Security
- Token Authentication
- Protected APIs

---

## Student Module

- Profile Completion
- Resume Upload
- Job Search
- Eligibility Checking
- Duplicate Application Prevention
- Placement History

---

## Company Module

- Company Verification
- Company Profile
- Logo Upload
- Placement Drive Management
- Interview Scheduling
- Candidate Tracking

---

## Admin Module

- Dashboard Statistics
- Company Approval
- Student Management
- Job Approval
- Placement Monitoring

---

## Background Tasks

Implemented using **Celery + Redis**

### Daily Reminder

Every morning eligible students receive reminder emails for placement drives closing the next day.

---

### Monthly Placement Report

Monthly HTML report containing:

- Total Drives
- Approved Drives
- Total Applications
- Selected Students
- Shortlisted Students
- Rejected Students
- Pending Applications

---

## Caching

Implemented using Flask-Caching.

Cached APIs:

- Student Profile
- Company Profile
- Dashboard Statistics
- Job Listings

---

## File Uploads

Student

- Resume Upload (PDF)

Company

- Company Logo Upload

Stored inside

```
backend/static/uploads/
```

---

# Database Models

## User

- id
- name
- email
- password
- role
- active

---

## Student

- student_code
- full_name
- branch
- year
- cgpa
- resume
- profile_completed

---

## Company

- company_code
- company_name
- website
- industry
- hr_name
- hr_email
- phone
- address
- logo
- status

---

## Job

- title
- description
- location
- salary_package
- eligibility
- deadline
- status
- is_active

---

## Application

- student
- job
- status
- interview_date
- interview_time
- interview_mode
- interview_link
- applied_at

---

# API Modules

```
/api/auth

/api/student

/api/company

/api/job

/api/application

/api/admin
```

---

# Ports

Backend

```
http://127.0.0.1:5000
```

Frontend

```
http://localhost:5173
```

Redis

```
localhost:6379
```

---

# Installation

## Backend

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install packages

```bash
pip install -r requirements.txt
```

Run backend

```bash
python app.py
```

---

## Frontend

Install dependencies

```bash
npm install
```

Run

```bash
npm run dev
```

---

# Celery Setup

Run Worker

```bash
celery -A celery_app:celery worker --pool=solo --loglevel=info
```

Run Beat Scheduler

```bash
celery -A celery_app:celery beat --loglevel=info
```

---

# Redis Setup

Install either

- Redis
or

- Memurai (Windows)

Start Redis Server

Default Port

```
6379
```

---

# Mail Configuration

Configure in `config.py`

```
MAIL_SERVER=
MAIL_PORT=
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_DEFAULT_SENDER=
```

---

# Default Credentials

Administrator

```
Email

admin@campuschaupal.com

Password

admin123
```

---

# Workflow

Student

```
Register

↓

Complete Profile

↓

Browse Jobs

↓

Apply

↓

Interview

↓

Selection
```

Company

```
Register

↓

Admin Approval

↓

Create Drives

↓

Receive Applications

↓

Schedule Interviews

↓

Update Status
```

Admin

```
Login

↓

Approve Companies

↓

Approve Jobs

↓

Monitor Portal
```

---

# Future Enhancements

- Real-time Notifications
- In-App Messaging
- Multi-College Support
- Placement Analytics Charts
- Resume Parsing
- AI Resume Matching
- JWT Refresh Tokens

---

# Developed For

Modern Application Development II

IIT Madras BS Degree Programme

---

# Author

Shashikant

CampusChaupal – Placement Portal