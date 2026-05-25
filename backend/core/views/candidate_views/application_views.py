from django.shortcuts import render, get_object_or_404
from core.models import Candidate, Application
from core.decorators import role_required


@role_required(['candidate'])
def candidate_applications_list(request):
    candidate = get_object_or_404(Candidate, user=request.user)

    applications = Application.objects.filter(
        candidate=candidate
    ).select_related('job', 'job__company')

    return render(request, 'core/candidate_dashboard/applications/list_applications.html', {
        'applications': applications
    })


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