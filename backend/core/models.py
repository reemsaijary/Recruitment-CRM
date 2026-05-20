from django.db import models


# This model stores company/client information
class Company(models.Model):
    company_name = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=200)
    email = models.EmailField()
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


# This model stores candidate information
class Candidate(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    linkedin_url = models.URLField(blank=True, null=True)
    skills = models.TextField()
    experience_years = models.IntegerField()
    current_position = models.CharField(max_length=200, blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)  # LinkedIn, referral, website
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


# This model stores job openings posted by companies
class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    required_skills = models.TextField()
    status = models.CharField(max_length=50, default="Open")
    job_type = models.CharField(max_length=100, blank=True, null=True)  # Full-time, Part-time, Remote
    salary_range = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_title


# This model connects a candidate with a job
class Application(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Screening', 'Screening'),
        ('Interview Scheduled', 'Interview Scheduled'),
        ('Interview Done', 'Interview Done'),
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


# This model stores interview information
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


# This model stores evaluation/feedback
class Evaluation(models.Model):
    RECOMMENDATION_CHOICES = [
        ('Hire', 'Hire'),
        ('Reject', 'Reject'),
        ('Maybe', 'Maybe'),
    ]

    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    score = models.IntegerField()
    recommendation = models.CharField(
        max_length=100,
        choices=RECOMMENDATION_CHOICES,
        blank=True,
        null=True
    )
    feedback = models.TextField()

    def __str__(self):
        return f"Evaluation for {self.application}"


# This model stores follow-up activities and reminders
class Activity(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)  # Call, Email, Follow-up, Reminder
    due_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.activity_type} - {self.application}"