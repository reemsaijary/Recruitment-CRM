from django.shortcuts import render, redirect, get_object_or_404
from core.models import Candidate


def candidates_list(request):
    candidates = Candidate.objects.all()

    return render(request, 'core/admin_dashboard/candidates/list_candidates.html', {
    'candidates': candidates
})


def add_candidate(request):
    if request.method == 'POST':
        Candidate.objects.create(
            full_name=request.POST.get('full_name'),
          
            phone=request.POST.get('phone'),
            linkedin_url=request.POST.get('linkedin_url'),
          
            experience_years=request.POST.get('experience_years'),
            current_position=request.POST.get('current_position'),
            source=request.POST.get('source'),
            notes=request.POST.get('notes')
        )

        return redirect('candidates_list')

    return render(request, 'core/admin_dashboard/candidates/add_candidate.html')


def candidate_details(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)

    return render(request, 'core/admin_dashboard/candidates/candidate_details.html', {
    'candidate': candidate
})

def edit_candidate(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)

    if request.method == 'POST':
        candidate.full_name = request.POST.get('full_name')
       
        candidate.phone = request.POST.get('phone')
        candidate.linkedin_url = request.POST.get('linkedin_url')
       
        candidate.experience_years = request.POST.get('experience_years')
        candidate.current_position = request.POST.get('current_position')
        candidate.source = request.POST.get('source')
        candidate.notes = request.POST.get('notes')
        candidate.save()

        return redirect('candidates_list')

    return render(request, 'core/admin_dashboard/candidates/edit_candidate.html', {
    'candidate': candidate
})


def delete_candidate(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)

    if request.method == 'POST':
        candidate.delete()
        return redirect('candidates_list')

    return render(request, 'core/admin_dashboard/candidates/delete_candidate.html', {
    'candidate': candidate
})