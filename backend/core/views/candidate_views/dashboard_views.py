from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def candidate_dashboard(request):

    if request.user.profile.role != 'candidate':
        return redirect('login')

    return render(request, 'core/candidate_dashboard/dashboard.html')