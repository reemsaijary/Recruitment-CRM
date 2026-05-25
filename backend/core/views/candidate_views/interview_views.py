from django.shortcuts import render, get_object_or_404
from core.models import Candidate, Interview
from core.decorators import role_required

#list
@role_required(['candidate'])
def candidate_interviews_list(request):
    candidate = get_object_or_404(Candidate, user=request.user)

    interviews = Interview.objects.filter(
        application__candidate=candidate
    ).select_related('application', 'application__job', 'application__job__company')

    return render(request, 'core/candidate_dashboard/interviews/list_interviews.html', {
        'interviews': interviews
    })

#show details
@role_required(['candidate'])
def candidate_interview_details(request, interview_id):
    candidate = get_object_or_404(Candidate, user=request.user)

    interview = get_object_or_404(
        Interview,
        id=interview_id,
        application__candidate=candidate
    )

    return render(request, 'core/candidate_dashboard/interviews/interview_details.html', {
        'interview': interview
    })