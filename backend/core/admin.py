from django.contrib import admin
from .models import Company, Candidate, Job, Application, Interview, Evaluation


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact_name', 'email', 'industry', 'country')
    search_fields = ('company_name', 'contact_name', 'email', 'industry', 'country')


class CandidateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'experience_years')
    search_fields = ('full_name', 'email', 'skills')


class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'location', 'status')
    search_fields = ('job_title', 'company__company_name', 'required_skills')
    list_filter = ('status', 'location')


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'job', 'status', 'applied_date')
    search_fields = ('candidate__full_name', 'job__job_title')
    list_filter = ('status', 'applied_date')


class InterviewAdmin(admin.ModelAdmin):
    list_display = ('application', 'interview_date', 'interview_type')
    search_fields = ('application__candidate__full_name', 'application__job__job_title')
    list_filter = ('interview_type', 'interview_date')


class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('application', 'score')
    search_fields = ('application__candidate__full_name', 'application__job__job_title')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Interview, InterviewAdmin)
admin.site.register(Evaluation, EvaluationAdmin)