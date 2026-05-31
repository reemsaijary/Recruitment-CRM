from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from core.models import Activity, Company
from core.decorators import role_required

#list
@role_required(['admin'])
def activities_list(request):
    activities = Activity.objects.all().select_related(
        'application',
        'application__candidate',
        'application__job',
        'application__job__company'
    ).order_by('-due_date')

    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    company_filter = request.GET.get('company', '')

    if search_query:
        activities = activities.filter(
            Q(application__candidate__full_name__icontains=search_query) |
            Q(application__job__job_title__icontains=search_query) |
            Q(application__job__company__company_name__icontains=search_query) |
            Q(activity_type__icontains=search_query) |
            Q(notes__icontains=search_query)
        )

    if status_filter:
        activities = activities.filter(status=status_filter)

    if company_filter:
        activities = activities.filter(application__job__company_id=company_filter)

    total_activities = Activity.objects.count()
    pending_count = Activity.objects.filter(status='Pending').count()
    completed_count = Activity.objects.filter(status='Completed').count()
    cancelled_count = Activity.objects.filter(status='Cancelled').count()

    companies = Company.objects.all().order_by('company_name')

    paginator = Paginator(activities, 8)
    page_number = request.GET.get('page')
    activities_page = paginator.get_page(page_number)

    return render(request, 'core/admin_dashboard/activities/list_activities.html', {
        'activities': activities_page,
        'search_query': search_query,
        'status_filter': status_filter,
        'company_filter': company_filter,
        'companies': companies,
        'status_choices': Activity.STATUS_CHOICES,
        'total_activities': total_activities,
        'pending_count': pending_count,
        'completed_count': completed_count,
        'cancelled_count': cancelled_count,
    })

#view
@role_required(['admin'])
def activity_details(request, activity_id):
    activity = get_object_or_404(
        Activity.objects.select_related(
            'application',
            'application__candidate',
            'application__job',
            'application__job__company'
        ),
        id=activity_id
    )

    return render(request, 'core/admin_dashboard/activities/activity_details.html', {
        'activity': activity
    })