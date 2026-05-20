# Recruitment CRM Database Design

## Overview
The database is designed for a recruitment CRM/ATS system. It manages companies, candidates, jobs, applications, interviews, evaluations, and follow-up activities.

## Main Relationship
Company → Job → Application ← Candidate

Application is the main table that connects candidates to jobs and tracks the hiring pipeline status.

## Tables

### Company
Stores company/client information.

Fields:
- company_name
- contact_name
- email
- phone
- website
- linkedin_url
- industry
- country
- company_size
- notes
- created_at

### Candidate
Stores candidate information.

Fields:
- full_name
- email
- phone
- linkedin_url
- skills
- experience_years
- current_position
- source
- notes
- created_at

### Job
Stores job openings posted by companies.

Fields:
- company
- job_title
- location
- required_skills
- status
- job_type
- salary_range
- description
- created_at

### Application
Connects a candidate with a job and tracks pipeline progress.

Fields:
- candidate
- job
- status
- applied_date
- notes
- updated_at

### Interview
Stores interview scheduling information.

Fields:
- application
- interview_date
- interview_type
- status
- notes

### Evaluation
Stores candidate evaluation and recruiter feedback.

Fields:
- application
- score
- recommendation
- feedback

### Activity
Stores follow-up tasks and reminders.

Fields:
- application
- activity_type
- due_date
- status
- notes