from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from core.models import Candidate, Application
from core.decorators import role_required

#list
@role_required(['candidate'])
def candidate_applications_list(request):
    candidate = get_object_or_404(Candidate, user=request.user)

    applications = Application.objects.filter(
        candidate=candidate
    ).select_related('job', 'job__company').order_by('-applied_date', '-id')

    search = request.GET.get('search', '')
    status = request.GET.get('status', '')

    if search:
        applications = applications.filter(
            Q(job__job_title__icontains=search) |
            Q(job__company__company_name__icontains=search) |
            Q(job__location__icontains=search)
        )

    if status:
        applications = applications.filter(status=status)

    all_applications = Application.objects.filter(candidate=candidate)

    total_applications = all_applications.count()
    applied_count = all_applications.filter(status='Applied').count()
    interview_count = all_applications.filter(status='Interview Scheduled').count()
    hired_count = all_applications.filter(status='Hired').count()
    rejected_count = all_applications.filter(status='Rejected').count()

    paginator = Paginator(applications, 5)
    page_number = request.GET.get('page')
    applications = paginator.get_page(page_number)

    return render(request, 'core/candidate_dashboard/applications/list_applications.html', {
        'applications': applications,
        'search': search,
        'status': status,
        'total_applications': total_applications,
        'applied_count': applied_count,
        'interview_count': interview_count,
        'hired_count': hired_count,
        'rejected_count': rejected_count,
    })

#show details
@role_required(['candidate'])
def candidate_application_details(request, application_id):
    candidate = get_object_or_404(Candidate, user=request.user)

    application = get_object_or_404(
        Application,
        id=application_id,
        candidate=candidate
    )

    return render(request, 'core/candidate_dashboard/applications/application_details.html', {
        'application': application
    })