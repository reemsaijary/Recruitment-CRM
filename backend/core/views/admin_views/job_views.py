from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404

from core.models import Job, Company, Application, Interview
from core.decorators import role_required

#list
@role_required(['admin'])
def jobs_list(request):
    jobs = Job.objects.all().select_related('company').annotate(
        applications_count=Count('application', distinct=True),
        interviews_count=Count('application__interview', distinct=True)
    ).order_by('-created_at')

    search_query = request.GET.get('search', '')
    company_filter = request.GET.get('company', '')
    status_filter = request.GET.get('status', '')
    type_filter = request.GET.get('job_type', '')

    if search_query:
        jobs = jobs.filter(
            Q(job_title__icontains=search_query) |
            Q(company__company_name__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(job_type__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    if company_filter:
        jobs = jobs.filter(company_id=company_filter)

    if status_filter:
        jobs = jobs.filter(status=status_filter)

    if type_filter:
        jobs = jobs.filter(job_type__icontains=type_filter)

    total_jobs = Job.objects.count()
    open_jobs = Job.objects.filter(status='Open').count()
    closed_jobs = Job.objects.filter(status='Closed').count()
    total_applications = Application.objects.count()

    companies = Company.objects.all().order_by('company_name')

    job_types = Job.objects.exclude(
        job_type__isnull=True
    ).exclude(
        job_type=''
    ).values_list('job_type', flat=True).distinct()

    paginator = Paginator(jobs, 8)
    page_number = request.GET.get('page')
    jobs_page = paginator.get_page(page_number)

    return render(request, 'core/admin_dashboard/jobs/list_jobs.html', {
        'jobs': jobs_page,
        'search_query': search_query,
        'company_filter': company_filter,
        'status_filter': status_filter,
        'type_filter': type_filter,
        'companies': companies,
        'job_types': job_types,
        'total_jobs': total_jobs,
        'open_jobs': open_jobs,
        'closed_jobs': closed_jobs,
        'total_applications': total_applications,
    })

#view detais
@role_required(['admin'])
def job_details(request, job_id):
    job = get_object_or_404(Job.objects.select_related('company'), id=job_id)

    applications = Application.objects.filter(
        job=job
    ).select_related('candidate').order_by('-applied_date')

    interviews = Interview.objects.filter(
        application__job=job
    ).select_related('application', 'application__candidate')

    shortlisted_count = applications.filter(status='Shortlisted').count()
    hired_count = applications.filter(status='Hired').count()

    return render(request, 'core/admin_dashboard/jobs/job_details.html', {
        'job': job,
        'applications': applications,
        'interviews': interviews,
        'applications_count': applications.count(),
        'interviews_count': interviews.count(),
        'shortlisted_count': shortlisted_count,
        'hired_count': hired_count,
    })