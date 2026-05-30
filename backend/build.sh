#!/usr/bin/env bash

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate

python manage.py shell << END
from django.contrib.auth.models import User
from core.models import Profile

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

print("Demo users with roles created successfully.")
END