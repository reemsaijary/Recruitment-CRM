from django.contrib import admin
from .models import Company, Candidate, Job, Application, Interview, Evaluation, Activity


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'company_name',
        'contact_name',
        'email',
        'phone',
        'website',
        'linkedin_url',
        'industry',
        'country',
        'company_size',
        'created_at',
    )
    search_fields = (
        'company_name',
        'contact_name',
        'email',
        'phone',
        'website',
        'linkedin_url',
        'industry',
        'country',
        'company_size',
        'notes',
    )
    list_filter = ('industry', 'country', 'company_size', 'created_at')


class CandidateAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone',
        'linkedin_url',
        'skills',
        'experience_years',
        'current_position',
        'source',
        'created_at',
    )
    search_fields = (
        'full_name',
        'email',
        'phone',
        'linkedin_url',
        'skills',
        'current_position',
        'source',
        'notes',
    )
    list_filter = ('source', 'experience_years', 'created_at')


class JobAdmin(admin.ModelAdmin):
    list_display = (
        'company',
        'job_title',
        'location',
        'required_skills',
        'status',
        'job_type',
        'salary_range',
        'created_at',
    )
    search_fields = (
        'company__company_name',
        'job_title',
        'location',
        'required_skills',
        'status',
        'job_type',
        'salary_range',
        'description',
    )
    list_filter = ('status', 'job_type', 'location', 'created_at')


class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'candidate',
        'job',
        'status',
        'applied_date',
        'updated_at',
    )
    search_fields = (
        'candidate__full_name',
        'job__job_title',
        'status',
        'notes',
    )
    list_filter = ('status', 'applied_date', 'updated_at')


class InterviewAdmin(admin.ModelAdmin):
    list_display = (
        'application',
        'interview_date',
        'interview_type',
        'status',
        'notes',
    )
    search_fields = (
        'application__candidate__full_name',
        'application__job__job_title',
        'interview_type',
        'status',
        'notes',
    )
    list_filter = ('status', 'interview_type', 'interview_date')


class EvaluationAdmin(admin.ModelAdmin):
    list_display = (
        'application',
        'score',
        'recommendation',
        'feedback',
    )
    search_fields = (
        'application__candidate__full_name',
        'application__job__job_title',
        'score',
        'recommendation',
        'feedback',
    )
    list_filter = ('recommendation', 'score')


class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        'application',
        'activity_type',
        'due_date',
        'status',
        'notes',
    )
    search_fields = (
        'application__candidate__full_name',
        'application__job__job_title',
        'activity_type',
        'status',
        'notes',
    )
    list_filter = ('status', 'activity_type', 'due_date')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Interview, InterviewAdmin)
admin.site.register(Evaluation, EvaluationAdmin)
admin.site.register(Activity, ActivityAdmin)