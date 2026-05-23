from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def company_dashboard(request):

    if request.user.profile.role != 'company':
        return redirect('login')

    return render(request, 'core/company_dashboard/dashboard.html')