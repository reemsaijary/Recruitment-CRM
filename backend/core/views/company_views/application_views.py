from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from core.models import Company, Application, Notification
from core.decorators import role_required
from django.urls import reverse

# list
@role_required(['company'])
def company_applications_list(request):
    company = get_object_or_404(Company, user=request.user)

    applications = Application.objects.filter(
        job__company=company
    ).select_related('candidate', 'job').order_by('-applied_date', '-id')

    search = request.GET.get('search', '')
    status = request.GET.get('status', '')

    if search:
        applications = applications.filter(
            Q(candidate__full_name__icontains=search) |
            Q(job__job_title__icontains=search)
        )

    if status:
        applications = applications.filter(status=status)

    all_applications = Application.objects.filter(job__company=company)

    total_applications = all_applications.count()
    applied_count = all_applications.filter(status='Applied').count()
    interview_count = all_applications.filter(status='Interview Scheduled').count()
    hired_count = all_applications.filter(status='Hired').count()
    rejected_count = all_applications.filter(status='Rejected').count()

    paginator = Paginator(applications, 5)
    page_number = request.GET.get('page')
    applications = paginator.get_page(page_number)

    return render(request, 'core/company_dashboard/applications/list_applications.html', {
        'applications': applications,
        'search': search,
        'status': status,
        'total_applications': total_applications,
        'applied_count': applied_count,
        'interview_count': interview_count,
        'hired_count': hired_count,
        'rejected_count': rejected_count,
    })


# show details
@role_required(['company'])
def company_application_details(request, application_id):
    company = get_object_or_404(Company, user=request.user)

    application = get_object_or_404(
        Application,
        id=application_id,
        job__company=company
    )

    if request.method == "POST":
        old_status = application.status
        new_status = request.POST.get("status")

        application.status = new_status
        application.save()

        if application.candidate.user and old_status != new_status:
            Notification.objects.create(
                user=application.candidate.user,
                title='Application Status Updated',
                message=f'Your application for {application.job.job_title} is now {new_status}.',
                url=reverse('candidate_application_details', args=[application.id]),
                notification_type='status'
            )

        return redirect('company_application_details', application_id=application.id)

    return render(request, 'core/company_dashboard/applications/application_details.html', {
        'application': application
    })


# kanban
@role_required(['company'])
def company_applications_kanban(request):
    company = get_object_or_404(Company, user=request.user)

    applications = Application.objects.filter(
        job__company=company
    ).select_related('candidate', 'job')

    statuses = [
        'Applied',
        'Screening',
        'Shortlisted',
        'Interview Scheduled',
        'Rejected',
        'Hired',
    ]

    kanban_data = {}

    for status in statuses:
        kanban_data[status] = applications.filter(status=status)

    return render(request, 'core/company_dashboard/applications/applications_kanban.html', {
        'kanban_data': kanban_data,
        'statuses': statuses,
    })


# update kanban status
@role_required(['company'])
def update_application_status_from_kanban(request, application_id, new_status):
    company = get_object_or_404(Company, user=request.user)

    application = get_object_or_404(
        Application,
        id=application_id,
        job__company=company
    )

    allowed_statuses = [
        'Applied',
        'Screening',
        'Shortlisted',
        'Interview Scheduled',
        'Rejected',
        'Hired',
    ]

    if new_status in allowed_statuses:
        old_status = application.status
        application.status = new_status
        application.save()

        if application.candidate.user and old_status != new_status:
           Notification.objects.create(
            user=application.candidate.user,
            title='Application Status Updated',
            message=f'Your application for {application.job.job_title} is now {new_status}.',
            url=reverse('candidate_application_details', args=[application.id]),
            notification_type='status'
        )

    return redirect('company_applications_kanban')