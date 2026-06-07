from django.contrib import admin
from .models import Profile, Company, Candidate, Job, Skill, Application, Interview, Evaluation, Activity, Notification


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    search_fields = ('user__username', 'user__email', 'role')
    list_filter = ('role',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'company_name',
        'contact_name',
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
        'user__email',
        'phone',
        'website',
        'linkedin_url',
        'industry',
        'country',
        'company_size',
        'notes',
    )
    list_filter = ('industry', 'country', 'company_size', 'created_at')


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'phone',
        'linkedin_url',
        'experience_years',
        'current_position',
        'source',
        'created_at',
    )
    search_fields = (
        'full_name',
        'user__email',
        'phone',
        'linkedin_url',
        'current_position',
        'source',
        'notes',
    )
    list_filter = ('source', 'experience_years', 'created_at')


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'company',
        'job_title',
        'location',
        'status',
        'job_type',
        'min_salary',
        'max_salary',
        'created_at',
    )
    search_fields = (
        'company__company_name',
        'job_title',
        'location',
        'status',
        'job_type',
        'description',
    )
    list_filter = ('status', 'job_type', 'location', 'created_at')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'skill_name',
        'candidate',
        'job',
    )
    search_fields = (
        'skill_name',
        'candidate__full_name',
        'job__job_title',
    )


@admin.register(Application)
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


@admin.register(Interview)
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


@admin.register(Evaluation)
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
        'recommendation',
        'feedback',
    )
    list_filter = ('recommendation', 'score')


@admin.register(Activity)
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

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'title',
        'notification_type',
        'is_read',
        'created_at',
    )

    search_fields = (
        'user__username',
        'title',
        'message',
        'notification_type',
    )

    list_filter = (
        'notification_type',
        'is_read',
        'created_at',
    )