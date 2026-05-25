from django.shortcuts import render, get_object_or_404
from core.models import Candidate, Job, Application, Interview
from core.decorators import role_required


@role_required(['candidate'])
def candidate_dashboard(request):
    candidate = get_object_or_404(Candidate, user=request.user)

    applications = Application.objects.filter(candidate=candidate)
    interviews = Interview.objects.filter(application__candidate=candidate)

    latest_application = applications.order_by('-applied_date').first()

    context = {
        'candidate': candidate,
        'available_jobs': Job.objects.filter(status='Open').count(),
        'my_applications': applications.count(),
        'scheduled_interviews': interviews.filter(status='Scheduled').count(),
        'latest_application': latest_application,
    }

    return render(request, 'core/candidate_dashboard/dashboard.html', context)