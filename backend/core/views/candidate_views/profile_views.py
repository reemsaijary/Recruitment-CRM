from django.shortcuts import render, redirect, get_object_or_404
from core.models import Candidate
from core.decorators import role_required

#profile
@role_required(['candidate'])
def candidate_profile(request):
    candidate = get_object_or_404(Candidate, user=request.user)

    return render(request, 'core/candidate_dashboard/profile/profile.html', {
        'candidate': candidate
    })

#edit
@role_required(['candidate'])
def edit_candidate_profile(request):
    candidate = get_object_or_404(Candidate, user=request.user)

    if request.method == 'POST':
        candidate.full_name = request.POST.get('full_name')
        candidate.phone = request.POST.get('phone')
        candidate.location = request.POST.get('location')
        candidate.current_position = request.POST.get('current_position')
        candidate.experience_years = request.POST.get('experience_years')
        candidate.linkedin_url = request.POST.get('linkedin_url')
        candidate.skills = request.POST.get('skills')
        candidate.notes = request.POST.get('notes')

        if request.FILES.get('cv'):
            candidate.cv = request.FILES.get('cv')

        candidate.save()

        return redirect('candidate_profile')

    return render(request, 'core/candidate_dashboard/profile/edit.html', {
        'candidate': candidate
    })