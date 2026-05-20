from django.shortcuts import render
from .models import Candidate, Company, Job, Application, Interview


def dashboard(request):

    total_candidates = Candidate.objects.count()
    total_companies = Company.objects.count()
    total_jobs = Job.objects.count()
    total_applications = Application.objects.count()
    total_interviews = Interview.objects.count()

    context = {
        'total_candidates': total_candidates,
        'total_companies': total_companies,
        'total_jobs': total_jobs,
        'total_applications': total_applications,
        'total_interviews': total_interviews,
    }

    return render(request, 'core/dashboard.html', context)