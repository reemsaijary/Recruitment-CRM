from django.shortcuts import render, redirect, get_object_or_404
from core.models import Company


# Display all companies
def companies_list(request):
    companies = Company.objects.all()

    return render(request, 'core/companies/list_companies.html', {
        'companies': companies
    })


# Add new company
def add_company(request):
    if request.method == 'POST':
        Company.objects.create(
            company_name=request.POST.get('company_name'),
            contact_name=request.POST.get('contact_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            website=request.POST.get('website'),
            linkedin_url=request.POST.get('linkedin_url'),
            industry=request.POST.get('industry'),
            country=request.POST.get('country'),
            company_size=request.POST.get('company_size'),
            notes=request.POST.get('notes')
        )

        return redirect('companies_list')

    return render(request, 'core/companies/add_company.html')


# Show company details
def company_details(request, company_id):
    company = get_object_or_404(Company, id=company_id)

    return render(request, 'core/companies/company_details.html', {
        'company': company
    })


# Edit company
def edit_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)

    if request.method == 'POST':
        company.company_name = request.POST.get('company_name')
        company.contact_name = request.POST.get('contact_name')
        company.email = request.POST.get('email')
        company.phone = request.POST.get('phone')
        company.website = request.POST.get('website')
        company.linkedin_url = request.POST.get('linkedin_url')
        company.industry = request.POST.get('industry')
        company.country = request.POST.get('country')
        company.company_size = request.POST.get('company_size')
        company.notes = request.POST.get('notes')
        company.save()

        return redirect('companies_list')

    return render(request, 'core/companies/edit_company.html', {
        'company': company
    })


# Delete company
def delete_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)

    if request.method == 'POST':
        company.delete()
        return redirect('companies_list')

    return render(request, 'core/companies/delete_company.html', {
        'company': company
    })