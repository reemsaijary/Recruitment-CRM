from django.shortcuts import render
from core.decorators import role_required
from core.models import Company, Job, Application, Interview


@role_required(['company'])
def company_dashboard(request):
    company = Company.objects.get(user=request.user)

    jobs = Job.objects.filter(company=company)
    applications = Application.objects.filter(job__company=company)
    interviews = Interview.objects.filter(application__job__company=company)

    context = {
        'company': company,
        'jobs_count': jobs.count(),
        'applications_count': applications.count(),
        'interviews_count': interviews.count(),
        'active_jobs_count': jobs.filter(status='Open').count(),
    }

    return render(request, 'core/company_dashboard/dashboard.html', context)