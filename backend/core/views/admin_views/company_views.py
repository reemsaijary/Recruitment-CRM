from django.shortcuts import render, redirect, get_object_or_404
from core.models import Company
from core.decorators import role_required
from django.contrib.auth.models import User
from core.models import Profile

# Display all companies
@role_required(['admin'])
def companies_list(request):
    companies = Company.objects.all()

    return render(request, 'core/admin_dashboard/companies/list_companies.html', {
        'companies': companies
    })


# Add new company
@role_required(['admin'])
def add_company(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # CHECK USERNAME
        if User.objects.filter(username=username).exists():
            return render(request,
                'core/admin_dashboard/companies/add_company.html',
                {'error': 'Username already exists'}
            )

        # CHECK EMAIL
        if User.objects.filter(email=email).exists():
            return render(request,
                'core/admin_dashboard/companies/add_company.html',
                {'error': 'Email already exists'}
            )

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


# Show company details
@role_required(['admin'])
def company_details(request, company_id):
    company = get_object_or_404(Company, id=company_id)

    return render(request, 'core/admin_dashboard/companies/company_details.html', {
        'company': company
    })


# Edit company
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

        return redirect('companies_list')

    return render(request, 'core/admin_dashboard/companies/edit_company.html', {
        'company': company
    })


# Delete company
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