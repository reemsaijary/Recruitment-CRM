from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from core.models import Candidate, Company, Application
from core.decorators import role_required


# list
@role_required(['company'])
def company_candidates_list(request):
    search_query = request.GET.get('search', '')
    experience_filter = request.GET.get('experience', '')

    candidates = Candidate.objects.all().order_by('-created_at')

    if search_query:
        candidates = candidates.filter(
            Q(full_name__icontains=search_query) |
            Q(current_position__icontains=search_query) |
            Q(skills__icontains=search_query) |
            Q(location__icontains=search_query)
        )

    if experience_filter == 'junior':
        candidates = candidates.filter(experience_years__lte=2)
    elif experience_filter == 'mid':
        candidates = candidates.filter(experience_years__gte=3, experience_years__lte=5)
    elif experience_filter == 'senior':
        candidates = candidates.filter(experience_years__gte=6)

    total_candidates = Candidate.objects.count()
    junior_candidates = Candidate.objects.filter(experience_years__lte=2).count()
    mid_candidates = Candidate.objects.filter(experience_years__gte=3, experience_years__lte=5).count()
    senior_candidates = Candidate.objects.filter(experience_years__gte=6).count()

    paginator = Paginator(candidates, 7)
    page_number = request.GET.get('page')
    candidates = paginator.get_page(page_number)

    return render(request, 'core/company_dashboard/candidates/list_candidates.html', {
        'candidates': candidates,
        'search_query': search_query,
        'experience_filter': experience_filter,
        'total_candidates': total_candidates,
        'junior_candidates': junior_candidates,
        'mid_candidates': mid_candidates,
        'senior_candidates': senior_candidates,
    })


# show details
@role_required(['company'])
def company_candidate_details(request, candidate_id):
    company = get_object_or_404(Company, user=request.user)

    candidate = get_object_or_404(Candidate, id=candidate_id)

    applications = Application.objects.filter(
        candidate=candidate,
        job__company=company
    ).select_related('job').order_by('-applied_date')

    return render(request, 'core/company_dashboard/candidates/candidate_details.html', {
        'candidate': candidate,
        'applications': applications
    })