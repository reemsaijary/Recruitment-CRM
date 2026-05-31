from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from core.models import Application, Company, Activity, Interview
from core.decorators import role_required

#list
@role_required(['admin'])
def applications_list(request):
    applications = Application.objects.all().select_related(
        'candidate',
        'job',
        'job__company'
    ).order_by('-updated_at')

    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    company_filter = request.GET.get('company', '')

    if search_query:
        applications = applications.filter(
            Q(candidate__full_name__icontains=search_query) |
            Q(job__job_title__icontains=search_query) |
            Q(job__company__company_name__icontains=search_query)
        )

    if status_filter:
        applications = applications.filter(status=status_filter)

    if company_filter:
        applications = applications.filter(job__company_id=company_filter)

    total_applications = Application.objects.count()
    applied_count = Application.objects.filter(status='Applied').count()
    screening_count = Application.objects.filter(status='Screening').count()
    interview_count = Application.objects.filter(
        status__in=['Interview Scheduled', 'Interview Done']
    ).count()
    hired_count = Application.objects.filter(status='Hired').count()
    rejected_count = Application.objects.filter(status='Rejected').count()

    companies = Company.objects.all().order_by('company_name')

    paginator = Paginator(applications, 8)
    page_number = request.GET.get('page')
    applications_page = paginator.get_page(page_number)

    return render(request, 'core/admin_dashboard/applications/list_applications.html', {
        'applications': applications_page,
        'search_query': search_query,
        'status_filter': status_filter,
        'company_filter': company_filter,
        'companies': companies,
        'status_choices': Application.STATUS_CHOICES,
        'total_applications': total_applications,
        'applied_count': applied_count,
        'screening_count': screening_count,
        'interview_count': interview_count,
        'hired_count': hired_count,
        'rejected_count': rejected_count,
    })

#view
@role_required(['admin'])
def application_details(request, application_id):
    application = get_object_or_404(
        Application.objects.select_related('candidate', 'job', 'job__company'),
        id=application_id
    )

    interviews = Interview.objects.filter(
        application=application
    ).order_by('-interview_date')

    activities = Activity.objects.filter(
        application=application
    ).order_by('-due_date')

    return render(request, 'core/admin_dashboard/applications/application_details.html', {
        'application': application,
        'interviews': interviews,
        'activities': activities,
    })