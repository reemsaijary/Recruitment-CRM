from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from core.models import Interview, Company
from core.decorators import role_required


@role_required(['admin'])
def interviews_list(request):
    interviews = Interview.objects.all().select_related(
        'application',
        'application__candidate',
        'application__job',
        'application__job__company'
    ).order_by('-interview_date')

    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    company_filter = request.GET.get('company', '')

    if search_query:
        interviews = interviews.filter(
            Q(application__candidate__full_name__icontains=search_query) |
            Q(application__job__job_title__icontains=search_query) |
            Q(application__job__company__company_name__icontains=search_query) |
            Q(interview_type__icontains=search_query)
        )

    if status_filter:
        interviews = interviews.filter(status=status_filter)

    if company_filter:
        interviews = interviews.filter(application__job__company_id=company_filter)

    total_interviews = Interview.objects.count()
    scheduled_interviews = Interview.objects.filter(status='Scheduled').count()
    completed_interviews = Interview.objects.filter(status='Completed').count()
    cancelled_interviews = Interview.objects.filter(status='Cancelled').count()

    companies = Company.objects.all().order_by('company_name')

    paginator = Paginator(interviews, 8)
    page_number = request.GET.get('page')
    interviews_page = paginator.get_page(page_number)

    return render(request, 'core/admin_dashboard/interviews/list_interviews.html', {
        'interviews': interviews_page,
        'search_query': search_query,
        'status_filter': status_filter,
        'company_filter': company_filter,
        'companies': companies,
        'status_choices': Interview.STATUS_CHOICES,
        'total_interviews': total_interviews,
        'scheduled_interviews': scheduled_interviews,
        'completed_interviews': completed_interviews,
        'cancelled_interviews': cancelled_interviews,
    })


@role_required(['admin'])
def interview_details(request, interview_id):
    interview = get_object_or_404(
        Interview.objects.select_related(
            'application',
            'application__candidate',
            'application__job',
            'application__job__company'
        ),
        id=interview_id
    )

    return render(request, 'core/admin_dashboard/interviews/interview_details.html', {
        'interview': interview
    })