from django.shortcuts import render
from django.db.models import Count

from core.models import Candidate, Company, Job, Application, Interview, Evaluation, Activity
from core.decorators import role_required


@role_required(['admin'])
def dashboard(request):
    recent_applications = Application.objects.select_related(
        'candidate',
        'job',
        'job__company'
    ).order_by('-applied_date')[:5]

    recent_activities = Activity.objects.select_related(
        'application',
        'application__candidate',
        'application__job'
    ).order_by('-due_date')[:5]

    context = {
        'candidates_count': Candidate.objects.count(),
        'companies_count': Company.objects.count(),
        'jobs_count': Job.objects.count(),
        'applications_count': Application.objects.count(),
        'interviews_count': Interview.objects.count(),
        'evaluations_count': Evaluation.objects.count(),
        'activities_count': Activity.objects.count(),

        'open_jobs_count': Job.objects.filter(status='Open').count(),
        'hired_count': Application.objects.filter(status='Hired').count(),
        'pending_activities_count': Activity.objects.filter(status='Pending').count(),
        'scheduled_interviews_count': Interview.objects.filter(status='Scheduled').count(),

        'recent_applications': recent_applications,
        'recent_activities': recent_activities,
    }

    return render(request, 'core/admin_dashboard/dashboard.html', context)