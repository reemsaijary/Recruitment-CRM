from django.db import models


# This model stores company/client information
class Company(models.Model):
    company_name = models.CharField(max_length=200)  # Company name
    contact_name = models.CharField(max_length=200)  # Person we contact in the company
    email = models.EmailField()  # Company/contact email
    phone = models.CharField(max_length=50)  # Company/contact phone number
    website = models.URLField(blank=True, null=True)  # Company website, optional
    linkedin_url = models.URLField(blank=True, null=True)  # Company LinkedIn link, optional
    industry = models.CharField(max_length=100)  # Example: IT, Healthcare, Finance
    country = models.CharField(max_length=100)  # Company country

    # This controls how the company appears in Django admin
    def __str__(self):
        return self.company_name


# This model stores candidate information
class Candidate(models.Model):
    full_name = models.CharField(max_length=200)  # Candidate full name
    email = models.EmailField()  # Candidate email
    phone = models.CharField(max_length=50)  # Candidate phone number
    linkedin_url = models.URLField(blank=True, null=True)  # Candidate LinkedIn link, optional
    skills = models.TextField()  # Candidate skills, example: Python, Django, React
    experience_years = models.IntegerField()  # Number of years of experience

    # This controls how the candidate appears in Django admin
    def __str__(self):
        return self.full_name


# This model stores job openings posted by companies
# Each job belongs to one company
class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)  # The company that posted the job
    job_title = models.CharField(max_length=200)  # Example: Backend Developer
    location = models.CharField(max_length=100)  # Job location
    required_skills = models.TextField()  # Skills needed for this job
    status = models.CharField(max_length=50, default="Open")  # Example: Open or Closed

    # This controls how the job appears in Django admin
    def __str__(self):
        return self.job_title


# This model connects a candidate with a job
# It tracks the candidate's hiring progress/pipeline status
class Application(models.Model):
    # Allowed application statuses
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Screening', 'Screening'),
        ('Interview Scheduled', 'Interview Scheduled'),
        ('Interview Done', 'Interview Done'),
        ('Offer Sent', 'Offer Sent'),
        ('Hired', 'Hired'),
        ('Rejected', 'Rejected'),
    ]

    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)  # Candidate who applied
    job = models.ForeignKey(Job, on_delete=models.CASCADE)  # Job the candidate applied to
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Applied')  # Current stage
    applied_date = models.DateField(auto_now_add=True)  # Automatically saves apply date

    # This controls how the application appears in Django admin
    def __str__(self):
        return f"{self.candidate.full_name} - {self.job.job_title}"


# This model stores interview information
# Each interview belongs to one application
class Interview(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)  # Related application
    interview_date = models.DateTimeField()  # Interview date and time
    interview_type = models.CharField(max_length=100)  # Example: Online, Phone, On-site
    notes = models.TextField(blank=True, null=True)  # Optional interview notes

    # This controls how the interview appears in Django admin
    def __str__(self):
        return f"Interview for {self.application}"


# This model stores evaluation/feedback after interview or screening
# Each evaluation belongs to one application
class Evaluation(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)  # Related application
    score = models.IntegerField()  # Candidate score
    feedback = models.TextField()  # Recruiter feedback

    # This controls how the evaluation appears in Django admin
    def __str__(self):
        return f"Evaluation for {self.application}"