from django.shortcuts import render, get_object_or_404
from core.models import Candidate
from core.decorators import role_required

#list 
@role_required(['company'])
def company_candidates_list(request):

    search_query = request.GET.get('search', '')

    candidates = Candidate.objects.all()

    if search_query:
        candidates = candidates.filter(
            full_name__icontains=search_query
        )

    return render(
        request,
        'core/company_dashboard/candidates/list_candidates.html',
        {
            'candidates': candidates,
            'search_query': search_query
        }
    )

#show details
@role_required(['company'])
def company_candidate_details(request, candidate_id):

    candidate = get_object_or_404(
        Candidate,
        id=candidate_id
    )

    return render(
        request,
        'core/company_dashboard/candidates/candidate_details.html',
        {
            'candidate': candidate
        }
    )