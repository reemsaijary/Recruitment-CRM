from django.core.paginator import Paginator
from django.db.models import Count, Avg, Q
from django.shortcuts import render, get_object_or_404

from core.models import Candidate, Application, Interview
from core.decorators import role_required

#list
@role_required(['admin'])
def candidates_list(request):
    candidates = Candidate.objects.all().select_related('user').annotate(
        applications_count=Count('application', distinct=True),
        interviews_count=Count('application__interview', distinct=True)
    ).order_by('-created_at')

    search_query = request.GET.get('search', '')
    location_filter = request.GET.get('location', '')
    experience_filter = request.GET.get('experience', '')

    if search_query:
        candidates = candidates.filter(
            Q(full_name__icontains=search_query) |
            Q(user__email__icontains=search_query) |
            Q(current_position__icontains=search_query) |
            Q(skills__icontains=search_query) |
            Q(location__icontains=search_query)
        )

    if location_filter:
        candidates = candidates.filter(location__icontains=location_filter)

    if experience_filter:
        candidates = candidates.filter(experience_years=experience_filter)

    total_candidates = Candidate.objects.count()
    total_applications = Application.objects.count()
    total_interviews = Interview.objects.count()
    average_experience = Candidate.objects.aggregate(
        avg_exp=Avg('experience_years')
    )['avg_exp'] or 0

    locations = Candidate.objects.exclude(
        location__isnull=True
    ).exclude(
        location=''
    ).values_list('location', flat=True).distinct()

    paginator = Paginator(candidates, 8)
    page_number = request.GET.get('page')
    candidates_page = paginator.get_page(page_number)

    return render(request, 'core/admin_dashboard/candidates/list_candidates.html', {
        'candidates': candidates_page,
        'search_query': search_query,
        'location_filter': location_filter,
        'experience_filter': experience_filter,
        'locations': locations,
        'total_candidates': total_candidates,
        'total_applications': total_applications,
        'total_interviews': total_interviews,
        'average_experience': round(average_experience, 1),
    })

#view
@role_required(['admin'])
def candidate_details(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)

    applications = Application.objects.filter(
        candidate=candidate
    ).select_related('job', 'job__company')

    interviews = Interview.objects.filter(
        application__candidate=candidate
    ).select_related('application', 'application__job')

    skills_count = 0
    if candidate.skills:
        skills_count = len([skill for skill in candidate.skills.split(',') if skill.strip()])

    return render(request, 'core/admin_dashboard/candidates/candidate_details.html', {
        'candidate': candidate,
        'applications': applications,
        'interviews': interviews,
        'skills_count': skills_count,
    })