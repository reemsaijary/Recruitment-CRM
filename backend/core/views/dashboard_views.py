from django.shortcuts import render
from core.models import Candidate, Company, Job, Application, Interview, Evaluation, Activity

def dashboard(request):
    context = {
        'candidates_count': Candidate.objects.count(),
        'companies_count': Company.objects.count(),
        'jobs_count': Job.objects.count(),
        'applications_count': Application.objects.count(),
        'interviews_count': Interview.objects.count(),
        'evaluations_count': Evaluation.objects.count(),
        'activities_count': Activity.objects.count(),
    }

    return render(request, 'core/dashboard.html', context)