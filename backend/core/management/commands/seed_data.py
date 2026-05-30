from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

from core.models import (
    Profile,
    Company,
    Candidate,
    Job,
    Application,
    Interview,
    Evaluation,
    Activity,
)


class Command(BaseCommand):
    help = "Populate the database with realistic mock recruitment CRM data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding recruitment CRM mock data...")

        default_password = "Demo12345"

        # -------------------------
        # 1. Admin User
        # -------------------------
        admin_user, created = User.objects.get_or_create(username="admin_demo")
        admin_user.set_password(default_password)
        admin_user.email = "admin_demo@demo.com"
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()

        admin_profile, created = Profile.objects.get_or_create(user=admin_user)
        admin_profile.role = "admin"
        admin_profile.save()

        # -------------------------
        # 2. Company Users + Companies
        # -------------------------
        companies_data = [
            {
                "username": "technova_admin",
                "company_name": "TechNova Solutions",
                "contact_name": "Omar Khaled",
                "phone": "+971501112233",
                "website": "https://technova.example.com",
                "linkedin_url": "https://linkedin.com/company/technova",
                "industry": "Software Development",
                "country": "UAE",
                "company_size": "11-50",
                "notes": "Growing tech company hiring developers and analysts.",
            },
            {
                "username": "cloudvision_admin",
                "company_name": "CloudVision Systems",
                "contact_name": "Fatima Al Mansoori",
                "phone": "+971552224444",
                "website": "https://cloudvision.example.com",
                "linkedin_url": "https://linkedin.com/company/cloudvision",
                "industry": "Cloud Services",
                "country": "UAE",
                "company_size": "11-50",
                "notes": "Cloud and DevOps solutions provider.",
            },
            {
                "username": "talentbridge_admin",
                "company_name": "TalentBridge Recruitment",
                "contact_name": "Sarah Williams",
                "phone": "+442071234567",
                "website": "https://talentbridge.example.com",
                "linkedin_url": "https://linkedin.com/company/talentbridge",
                "industry": "Staffing and Recruiting",
                "country": "UK",
                "company_size": "51-100",
                "notes": "Recruitment agency focused on tech and business roles.",
            },
        ]

        companies = []

        for data in companies_data:
            company_user, created = User.objects.get_or_create(username=data["username"])
            company_user.set_password(default_password)
            company_user.email = f'{data["username"]}@demo.com'
            company_user.is_staff = False
            company_user.is_superuser = False
            company_user.save()

            profile, created = Profile.objects.get_or_create(user=company_user)
            profile.role = "company"
            profile.save()

            company, created = Company.objects.get_or_create(
                company_name=data["company_name"],
                defaults={
                    "user": company_user,
                    "contact_name": data["contact_name"],
                    "phone": data["phone"],
                    "website": data["website"],
                    "linkedin_url": data["linkedin_url"],
                    "industry": data["industry"],
                    "country": data["country"],
                    "company_size": data["company_size"],
                    "notes": data["notes"],
                }
            )

            company.user = company_user
            company.save()
            companies.append(company)

        # -------------------------
        # 3. Candidate Demo User
        # -------------------------
        candidate_user, created = User.objects.get_or_create(username="candidate_demo")
        candidate_user.set_password(default_password)
        candidate_user.email = "candidate_demo@demo.com"
        candidate_user.is_staff = False
        candidate_user.is_superuser = False
        candidate_user.save()

        candidate_profile, created = Profile.objects.get_or_create(user=candidate_user)
        candidate_profile.role = "candidate"
        candidate_profile.save()

        # -------------------------
        # 4. Candidates
        # -------------------------
        candidates_data = [
            {
                "full_name": "Candidate Demo",
                "user": candidate_user,
                "phone": "00000000",
                "location": "Lebanon",
                "skills": "Python, Django, SQL",
                "experience_years": 1,
                "current_position": "Junior Developer",
                "source": "Demo",
            },
            {
                "full_name": "John Smith",
                "user": None,
                "phone": "+447700900111",
                "location": "London",
                "skills": "HTML, CSS, JavaScript, React",
                "experience_years": 3,
                "current_position": "Frontend Developer",
                "source": "LinkedIn",
            },
            {
                "full_name": "Sarah Johnson",
                "user": None,
                "phone": "+447700900222",
                "location": "Manchester",
                "skills": "Python, Django, REST API, PostgreSQL",
                "experience_years": 5,
                "current_position": "Backend Developer",
                "source": "Referral",
            },
            {
                "full_name": "Ahmed Hassan",
                "user": None,
                "phone": "+971501234567",
                "location": "Dubai",
                "skills": "Laravel, PHP, MySQL, Bootstrap",
                "experience_years": 4,
                "current_position": "Full Stack Developer",
                "source": "LinkedIn",
            },
            {
                "full_name": "Fatima Ali",
                "user": None,
                "phone": "+966501234567",
                "location": "Riyadh",
                "skills": "Excel, SQL, Power BI, Python",
                "experience_years": 2,
                "current_position": "Data Analyst",
                "source": "Job Board",
            },
            {
                "full_name": "Maya Brown",
                "user": None,
                "phone": "+447700900333",
                "location": "London",
                "skills": "Figma, UI/UX, Wireframes, Prototyping",
                "experience_years": 3,
                "current_position": "UI/UX Designer",
                "source": "LinkedIn",
            },
            {
                "full_name": "Khaled Nasser",
                "user": None,
                "phone": "+971509876543",
                "location": "Abu Dhabi",
                "skills": "AWS, Docker, Linux, CI/CD",
                "experience_years": 4,
                "current_position": "DevOps Engineer",
                "source": "Apollo",
            },
            {
                "full_name": "Lina Haddad",
                "user": None,
                "phone": "+96170111222",
                "location": "Beirut",
                "skills": "Java, Spring Boot, SQL",
                "experience_years": 2,
                "current_position": "Junior Backend Developer",
                "source": "Website",
            },
            {
                "full_name": "Mohammed Omar",
                "user": None,
                "phone": "+966551112233",
                "location": "Jeddah",
                "skills": "React, Node.js, MongoDB",
                "experience_years": 3,
                "current_position": "Full Stack Developer",
                "source": "LinkedIn",
            },
            {
                "full_name": "Nour Saleh",
                "user": None,
                "phone": "+971558887777",
                "location": "Sharjah",
                "skills": "QA Testing, Selenium, Manual Testing",
                "experience_years": 2,
                "current_position": "QA Tester",
                "source": "Referral",
            },
        ]

        candidates = []

        for data in candidates_data:
            candidate, created = Candidate.objects.get_or_create(
                full_name=data["full_name"],
                defaults={
                    "user": data["user"],
                    "phone": data["phone"],
                    "linkedin_url": "",
                    "experience_years": data["experience_years"],
                    "location": data["location"],
                    "skills": data["skills"],
                    "current_position": data["current_position"],
                    "source": data["source"],
                    "notes": f'{data["full_name"]} is mock candidate data for testing.',
                }
            )

            if data["user"] is not None:
                candidate.user = data["user"]
                candidate.save()

            candidates.append(candidate)

        # -------------------------
        # 5. Jobs
        # -------------------------
        jobs_data = [
            {
                "company": companies[0],
                "job_title": "Frontend Developer",
                "location": "Dubai",
                "status": "Open",
                "job_type": "Full-time",
                "min_salary": 1200,
                "max_salary": 2200,
                "description": "Build responsive frontend pages using HTML, CSS, JavaScript, and React.",
            },
            {
                "company": companies[0],
                "job_title": "Backend Developer",
                "location": "Dubai",
                "status": "Open",
                "job_type": "Full-time",
                "min_salary": 1500,
                "max_salary": 2800,
                "description": "Develop backend APIs using Django, REST framework, and PostgreSQL.",
            },
            {
                "company": companies[0],
                "job_title": "Data Analyst",
                "location": "Dubai",
                "status": "Open",
                "job_type": "Hybrid",
                "min_salary": 1300,
                "max_salary": 2400,
                "description": "Analyze data, prepare reports, and create dashboards.",
            },
            {
                "company": companies[1],
                "job_title": "DevOps Engineer",
                "location": "Abu Dhabi",
                "status": "Open",
                "job_type": "Hybrid",
                "min_salary": 2200,
                "max_salary": 4000,
                "description": "Manage cloud infrastructure, Docker containers, and CI/CD pipelines.",
            },
            {
                "company": companies[1],
                "job_title": "Cloud Engineer",
                "location": "Abu Dhabi",
                "status": "Open",
                "job_type": "Full-time",
                "min_salary": 2000,
                "max_salary": 3600,
                "description": "Work with AWS services, cloud monitoring, and deployment automation.",
            },
            {
                "company": companies[1],
                "job_title": "QA Tester",
                "location": "Abu Dhabi",
                "status": "Open",
                "job_type": "Full-time",
                "min_salary": 1000,
                "max_salary": 1800,
                "description": "Test web applications and document bugs clearly.",
            },
            {
                "company": companies[2],
                "job_title": "Technical Recruiter",
                "location": "London",
                "status": "Open",
                "job_type": "Remote",
                "min_salary": 1300,
                "max_salary": 2300,
                "description": "Source, screen, and communicate with technical candidates.",
            },
            {
                "company": companies[2],
                "job_title": "Recruitment Coordinator",
                "location": "Manchester",
                "status": "Open",
                "job_type": "Hybrid",
                "min_salary": 1200,
                "max_salary": 2000,
                "description": "Coordinate interviews, follow-ups, and recruitment activities.",
            },
            {
                "company": companies[2],
                "job_title": "UI/UX Designer",
                "location": "London",
                "status": "Open",
                "job_type": "Remote",
                "min_salary": 1800,
                "max_salary": 3000,
                "description": "Design user-friendly dashboards and candidate workflows.",
            },
        ]

        jobs = []

        for data in jobs_data:
            job, created = Job.objects.get_or_create(
                company=data["company"],
                job_title=data["job_title"],
                defaults={
                    "location": data["location"],
                    "status": data["status"],
                    "job_type": data["job_type"],
                    "min_salary": data["min_salary"],
                    "max_salary": data["max_salary"],
                    "description": data["description"],
                }
            )
            jobs.append(job)

        # -------------------------
        # 6. Applications
        # -------------------------
        application_data = [
            (candidates[0], jobs[0], "Applied"),
            (candidates[1], jobs[0], "Shortlisted"),
            (candidates[2], jobs[1], "Interview Scheduled"),
            (candidates[3], jobs[1], "Screening"),
            (candidates[4], jobs[2], "Evaluated"),
            (candidates[5], jobs[8], "Applied"),
            (candidates[6], jobs[3], "Interview Scheduled"),
            (candidates[7], jobs[1], "Rejected"),
            (candidates[8], jobs[4], "Offer Sent"),
            (candidates[9], jobs[5], "Screening"),
            (candidates[1], jobs[6], "Applied"),
            (candidates[2], jobs[6], "Shortlisted"),
            (candidates[3], jobs[7], "Interview Done"),
            (candidates[4], jobs[7], "Hired"),
            (candidates[5], jobs[8], "Interview Scheduled"),
            (candidates[6], jobs[4], "Evaluated"),
            (candidates[8], jobs[0], "Applied"),
            (candidates[9], jobs[3], "Shortlisted"),
        ]

        applications = []

        for candidate, job, status in application_data:
            application, created = Application.objects.get_or_create(
                candidate=candidate,
                job=job,
                defaults={
                    "status": status,
                    "notes": f"{candidate.full_name} applied to {job.job_title}. Current status: {status}.",
                }
            )

            if not created:
                application.status = status
                application.save()

            applications.append(application)

        # -------------------------
        # 7. Interviews
        # -------------------------
        interview_types = ["Online", "Phone Call", "On-site", "Technical Interview"]

        for index, application in enumerate(applications[:10]):
            Interview.objects.get_or_create(
                application=application,
                defaults={
                    "interview_date": timezone.now() + timedelta(days=index + 1),
                    "interview_type": interview_types[index % len(interview_types)],
                    "status": "Scheduled" if index % 2 == 0 else "Completed",
                    "notes": "Mock interview created for CRM testing.",
                }
            )

        # -------------------------
        # 8. Evaluations
        # -------------------------
        recommendations = ["Hire", "Reject", "Maybe"]

        for index, application in enumerate(applications[:10]):
            Evaluation.objects.get_or_create(
                application=application,
                defaults={
                    "score": 60 + (index * 4),
                    "recommendation": recommendations[index % len(recommendations)],
                    "feedback": "Mock evaluation feedback for testing candidate assessment.",
                }
            )

        # -------------------------
        # 9. Activities
        # -------------------------
        activity_types = [
            "CV Review",
            "Candidate Follow-up",
            "Client Feedback Reminder",
            "Interview Reminder",
            "Offer Follow-up",
        ]

        for index, application in enumerate(applications[:12]):
            Activity.objects.get_or_create(
                application=application,
                activity_type=activity_types[index % len(activity_types)],
                defaults={
                    "due_date": timezone.now() + timedelta(days=index + 2),
                    "status": "Pending" if index % 2 == 0 else "Completed",
                    "notes": "Mock CRM activity for testing follow-up workflow.",
                }
            )

        self.stdout.write(self.style.SUCCESS("Mock recruitment CRM data created successfully."))
        self.stdout.write(self.style.SUCCESS("Admin login: admin_demo / Demo12345"))
        self.stdout.write(self.style.SUCCESS("Company logins: technova_admin, cloudvision_admin, talentbridge_admin / Demo12345"))
        self.stdout.write(self.style.SUCCESS("Candidate login: candidate_demo / Demo12345"))