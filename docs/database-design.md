# Recruitment CRM Database Design

## Overview

The Recruitment CRM database is designed to support a multi-role recruitment management platform.

The system supports:

- Administrators
- Companies
- Candidates

and manages the complete recruitment lifecycle.

---

## Main Relationships

Company
→ Job
→ Application
← Candidate

Application
→ Interview

Application
→ Evaluation

Application
→ Activity

User
→ Profile

---

# User

Django authentication user.

## Purpose

Stores login credentials.

### Key Fields

- username
- email
- password

---

# Profile

Extends the User model.

## Purpose

Stores platform role information.

### Fields

- user
- role

### Roles

- Admin
- Company
- Candidate

---

# Company

Stores company information.

### Fields

- user
- company_name
- contact_name
- phone
- website
- linkedin_url
- industry
- country
- company_size
- notes
- created_at

---

# Candidate

Stores candidate information.

### Fields

- user
- full_name
- phone
- linkedin_url
- skills
- experience_years
- current_position
- location
- source
- notes
- cv
- created_at

---

# Job

Stores job openings.

### Fields

- company
- job_title
- job_type
- location
- status
- min_salary
- max_salary
- description
- created_at

---

# Application

Connects candidates with jobs.

### Statuses

- Applied
- Screening
- Shortlisted
- Interview Scheduled
- Interview Done
- Evaluated
- Offer Sent
- Hired
- Rejected

### Fields

- candidate
- job
- status
- notes
- applied_date
- updated_at

---

# Interview

Stores interview information.

### Fields

- application
- interview_date
- interview_type
- status
- notes

---

# Evaluation

Stores evaluation data.

### Fields

- application
- score
- recommendation
- feedback

---

# Activity

Stores follow-up tasks.

### Fields

- application
- activity_type
- due_date
- status
- notes

---

# Notification

Stores system notifications.

### Fields

- user
- title
- message
- notification_type
- is_read
- created_at