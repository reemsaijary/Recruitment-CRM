from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from core.models import Evaluation, Company
from core.decorators import role_required

#list
@role_required(['admin'])
def evaluations_list(request):
    evaluations = Evaluation.objects.all().select_related(
        'application',
        'application__candidate',
        'application__job',
        'application__job__company'
    ).order_by('-id')

    search_query = request.GET.get('search', '')
    recommendation_filter = request.GET.get('recommendation', '')
    company_filter = request.GET.get('company', '')

    if search_query:
        evaluations = evaluations.filter(
            Q(application__candidate__full_name__icontains=search_query) |
            Q(application__job__job_title__icontains=search_query) |
            Q(application__job__company__company_name__icontains=search_query) |
            Q(feedback__icontains=search_query)
        )

    if recommendation_filter:
        evaluations = evaluations.filter(recommendation=recommendation_filter)

    if company_filter:
        evaluations = evaluations.filter(application__job__company_id=company_filter)

    total_evaluations = Evaluation.objects.count()
    hire_count = Evaluation.objects.filter(recommendation='Hire').count()
    reject_count = Evaluation.objects.filter(recommendation='Reject').count()
    maybe_count = Evaluation.objects.filter(recommendation='Maybe').count()

    companies = Company.objects.all().order_by('company_name')

    paginator = Paginator(evaluations, 8)
    page_number = request.GET.get('page')
    evaluations_page = paginator.get_page(page_number)

    return render(request, 'core/admin_dashboard/evaluations/list_evaluations.html', {
        'evaluations': evaluations_page,
        'search_query': search_query,
        'recommendation_filter': recommendation_filter,
        'company_filter': company_filter,
        'companies': companies,
        'recommendation_choices': Evaluation.RECOMMENDATION_CHOICES,
        'total_evaluations': total_evaluations,
        'hire_count': hire_count,
        'reject_count': reject_count,
        'maybe_count': maybe_count,
    })

#view 
@role_required(['admin'])
def evaluation_details(request, evaluation_id):
    evaluation = get_object_or_404(
        Evaluation.objects.select_related(
            'application',
            'application__candidate',
            'application__job',
            'application__job__company'
        ),
        id=evaluation_id
    )

    return render(request, 'core/admin_dashboard/evaluations/evaluation_details.html', {
        'evaluation': evaluation
    })