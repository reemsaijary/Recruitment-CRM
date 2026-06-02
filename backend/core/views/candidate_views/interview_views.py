from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from core.models import Candidate, Interview
from core.decorators import role_required


# list
@role_required(['candidate'])
def candidate_interviews_list(request):
    candidate = get_object_or_404(Candidate, user=request.user)

    interviews = Interview.objects.filter(
        application__candidate=candidate
    ).select_related(
        'application',
        'application__job',
        'application__job__company'
    ).order_by('-interview_date')

    search = request.GET.get('search', '')
    status = request.GET.get('status', '')

    if search:
        interviews = interviews.filter(
            Q(application__job__job_title__icontains=search) |
            Q(application__job__company__company_name__icontains=search) |
            Q(interview_type__icontains=search)
        )

    if status:
        interviews = interviews.filter(status=status)

    all_interviews = Interview.objects.filter(application__candidate=candidate)

    total_interviews = all_interviews.count()
    scheduled_count = all_interviews.filter(status='Scheduled').count()
    completed_count = all_interviews.filter(status='Completed').count()
    cancelled_count = all_interviews.filter(status='Cancelled').count()

    paginator = Paginator(interviews, 5)
    page_number = request.GET.get('page')
    interviews = paginator.get_page(page_number)

    return render(request, 'core/candidate_dashboard/interviews/list_interviews.html', {
        'interviews': interviews,
        'search': search,
        'status': status,
        'total_interviews': total_interviews,
        'scheduled_count': scheduled_count,
        'completed_count': completed_count,
        'cancelled_count': cancelled_count,
    })


# show details
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