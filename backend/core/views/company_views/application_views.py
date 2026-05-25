from django.shortcuts import render, get_object_or_404
from core.models import Company, Application
from core.decorators import role_required


@role_required(['company'])
def company_applications_list(request):
    company = get_object_or_404(Company, user=request.user)

    applications = Application.objects.filter(
        job__company=company
    ).select_related('candidate', 'job')

    return render(request, 'core/company_dashboard/applications/list_applications.html', {
        'applications': applications
    })


@role_required(['company'])
def company_application_details(request, application_id):
    company = get_object_or_404(Company, user=request.user)

    application = get_object_or_404(
        Application,
        id=application_id,
        job__company=company
    )

    return render(request, 'core/company_dashboard/applications/application_details.html', {
        'application': application
    })