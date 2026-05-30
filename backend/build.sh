#!/usr/bin/env bash

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate

python manage.py shell << END
from django.contrib.auth.models import User
from core.models import Profile, Candidate, Company

demo_users = [
    ("admin_demo", "admin", True, True),
    ("company_demo", "company", False, False),
    ("candidate_demo", "candidate", False, False),
]

for username, role, is_staff, is_superuser in demo_users:
    user, created = User.objects.get_or_create(username=username)
    user.set_password("Demo12345")
    user.email = username + "@demo.com"
    user.is_staff = is_staff
    user.is_superuser = is_superuser
    user.save()

    profile, created = Profile.objects.get_or_create(user=user)
    profile.role = role
    profile.save()

    if role == "candidate":
        Candidate.objects.get_or_create(
            user=user,
            defaults={
                "full_name": "Candidate Demo",
                "phone": "00000000",
                "linkedin_url": "",
                "experience_years": 1,
                "location": "Lebanon",
                "skills": "Python, Django, SQL",
                "current_position": "Junior Developer",
                "source": "Demo",
                "notes": "Demo candidate account"
            }
        )

    if role == "company":
        Company.objects.get_or_create(
            user=user,
            defaults={
                "company_name": "Demo Company",
                "contact_name": "Company Demo",
                "phone": "00000000",
                "website": "",
                "linkedin_url": "",
                "industry": "Recruitment",
                "country": "Lebanon",
                "company_size": "10-50",
                "notes": "Demo company account"
            }
        )

print("Demo users, profiles, candidate, and company records created successfully.")
END