from django.shortcuts import render
from core.decorators import role_required


@role_required(['company'])
def company_dashboard(request):
    return render(request, 'core/company_dashboard/dashboard.html')