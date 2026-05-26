from django.shortcuts import render, get_object_or_404, redirect
from core.models import Company, Application
from core.decorators import role_required

#list
@role_required(['company'])
def company_applications_list(request):
    company = get_object_or_404(Company, user=request.user)

    applications = Application.objects.filter(
        job__company=company
    ).select_related('candidate', 'job')

    return render(request, 'core/company_dashboard/applications/list_applications.html', {
        'applications': applications
    })

#show details
@role_required(['company'])
def company_application_details(request, application_id):
    company = get_object_or_404(Company, user=request.user)

    application = get_object_or_404(
        Application,
        id=application_id,
        job__company=company
    )

    if request.method == "POST":
        application.status = request.POST.get("status")
        application.save()
        return redirect('company_application_details', application_id=application.id)

    return render(request, 'core/company_dashboard/applications/application_details.html', {
        'application': application
    })

#kanbaan
def company_applications_kanban(request):

    company = Company.objects.get(user=request.user)

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

#update kanbaan status
def update_application_status_from_kanban(request, application_id, new_status):
    company = Company.objects.get(user=request.user)
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
        application.status = new_status
        application.save()

    return redirect('company_applications_kanban')