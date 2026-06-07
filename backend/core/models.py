from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('company', 'Company'),
        ('candidate', 'Candidate'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    company_name = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    website = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    industry = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    company_size = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name


class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    linkedin_url = models.URLField(blank=True, null=True)
    experience_years = models.IntegerField()
    
    cv = models.FileField(upload_to='candidate_cvs/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)

    current_position = models.CharField(max_length=200, blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default="Open")
    job_type = models.CharField(max_length=100, blank=True, null=True)
    min_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    max_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_title


class Skill(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True, blank=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True)
    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_name


class Application(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Screening', 'Screening'),
        ('Shortlisted', 'Shortlisted'),
        ('Interview Scheduled', 'Interview Scheduled'),
        ('Interview Done', 'Interview Done'),
        ('Evaluated', 'Evaluated'),
        ('Offer Sent', 'Offer Sent'),
        ('Hired', 'Hired'),
        ('Rejected', 'Rejected'),
    ]

    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Applied')
    applied_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.candidate.full_name} - {self.job.job_title}"


class Interview(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    interview_date = models.DateTimeField()
    interview_type = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Scheduled')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Interview for {self.application}"


class Evaluation(models.Model):
    RECOMMENDATION_CHOICES = [
        ('Hire', 'Hire'),
        ('Reject', 'Reject'),
        ('Maybe', 'Maybe'),
    ]

    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    score = models.IntegerField()
    recommendation = models.CharField(max_length=100, choices=RECOMMENDATION_CHOICES, blank=True, null=True)
    feedback = models.TextField()

    def __str__(self):
        return f"Evaluation for {self.application}"


class Activity(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.activity_type} - {self.application}"
    
class Notification(models.Model):
    TYPE_CHOICES = [
        ('application', 'Application'),
        ('interview', 'Interview'),
        ('status', 'Status Update'),
        ('system', 'System'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    title = models.CharField(max_length=200)
    message = models.TextField()
    notification_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='system')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title