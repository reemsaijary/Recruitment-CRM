from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from core.models import Company, Profile, Job, Application, Interview
from core.decorators import role_required

#list
@role_required(['admin'])
def companies_list(request):
    companies = Company.objects.all().select_related('user').annotate(
        jobs_count=Count('job', distinct=True),
        applications_count=Count('job__application', distinct=True),
        interviews_count=Count('job__application__interview', distinct=True)
    ).order_by('-created_at')

    search_query = request.GET.get('search', '')
    country_filter = request.GET.get('country', '')
    industry_filter = request.GET.get('industry', '')

    if search_query:
        companies = companies.filter(
            Q(company_name__icontains=search_query) |
            Q(contact_name__icontains=search_query) |
            Q(user__email__icontains=search_query) |
            Q(user__username__icontains=search_query) |
            Q(industry__icontains=search_query) |
            Q(country__icontains=search_query)
        )

    if country_filter:
        companies = companies.filter(country__icontains=country_filter)

    if industry_filter:
        companies = companies.filter(industry__icontains=industry_filter)

    total_companies = Company.objects.count()
    total_jobs = Job.objects.count()
    total_applications = Application.objects.count()
    total_interviews = Interview.objects.count()

    countries = Company.objects.exclude(country__isnull=True).exclude(country='').values_list(
        'country', flat=True
    ).distinct()

    industries = Company.objects.exclude(industry__isnull=True).exclude(industry='').values_list(
        'industry', flat=True
    ).distinct()

    paginator = Paginator(companies, 6)
    page_number = request.GET.get('page')
    companies_page = paginator.get_page(page_number)

    return render(request, 'core/admin_dashboard/companies/list_companies.html', {
        'companies': companies_page,
        'search_query': search_query,
        'country_filter': country_filter,
        'industry_filter': industry_filter,
        'countries': countries,
        'industries': industries,
        'total_companies': total_companies,
        'total_jobs': total_jobs,
        'total_applications': total_applications,
        'total_interviews': total_interviews,
    })

#add
@role_required(['admin'])
def add_company(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'core/admin_dashboard/companies/add_company.html', {
                'error': 'Username already exists'
            })

        if User.objects.filter(email=email).exists():
            return render(request, 'core/admin_dashboard/companies/add_company.html', {
                'error': 'Email already exists'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        Profile.objects.create(
            user=user,
            role='company'
        )

        Company.objects.create(
            user=user,
            company_name=request.POST.get('company_name'),
            contact_name=request.POST.get('contact_name'),
            phone=request.POST.get('phone'),
            website=request.POST.get('website'),
            linkedin_url=request.POST.get('linkedin_url'),
            industry=request.POST.get('industry'),
            country=request.POST.get('country'),
            company_size=request.POST.get('company_size'),
            notes=request.POST.get('notes')
        )

        return redirect('companies_list')

    return render(request, 'core/admin_dashboard/companies/add_company.html')

#view
@role_required(['admin'])
def company_details(request, company_id):
    company = get_object_or_404(Company, id=company_id)

    jobs = Job.objects.filter(company=company).order_by('-created_at')

    applications = Application.objects.filter(
        job__company=company
    ).select_related('candidate', 'job').order_by('-applied_date')

    interviews = Interview.objects.filter(
        application__job__company=company
    ).select_related('application', 'application__job')

    return render(request, 'core/admin_dashboard/companies/company_details.html', {
        'company': company,
        'jobs': jobs,
        'applications': applications,
        'interviews': interviews,
        'jobs_count': jobs.count(),
        'applications_count': applications.count(),
        'interviews_count': interviews.count(),
    })

#uodate
@role_required(['admin'])
def edit_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)

    if request.method == 'POST':
        company.company_name = request.POST.get('company_name')
        company.contact_name = request.POST.get('contact_name')
        company.phone = request.POST.get('phone')
        company.website = request.POST.get('website')
        company.linkedin_url = request.POST.get('linkedin_url')
        company.industry = request.POST.get('industry')
        company.country = request.POST.get('country')
        company.company_size = request.POST.get('company_size')
        company.notes = request.POST.get('notes')
        company.save()

        if company.user:
            company.user.username = request.POST.get('username')
            company.user.email = request.POST.get('email')
            company.user.save()

        return redirect('companies_list')

    return render(request, 'core/admin_dashboard/companies/edit_company.html', {
        'company': company
    })

#delete
@role_required(['admin'])
def delete_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)

    if request.method == 'POST':
        if company.user:
            company.user.delete()
        else:
            company.delete()

        return redirect('companies_list')

    return render(request, 'core/admin_dashboard/companies/delete_company.html', {
        'company': company
    })