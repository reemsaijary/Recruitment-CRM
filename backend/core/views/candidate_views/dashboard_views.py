from django.shortcuts import render
from core.decorators import role_required


@role_required(['candidate'])
def candidate_dashboard(request):
    return render(request, 'core/candidate_dashboard/dashboard.html')