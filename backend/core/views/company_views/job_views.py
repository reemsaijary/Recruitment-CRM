from django.shortcuts import render, redirect, get_object_or_404
from core.models import Company, Job
from core.decorators import role_required

#list job
@role_required(['company'])
def company_jobs_list(request):
    company = get_object_or_404(Company, user=request.user)
    jobs = Job.objects.filter(company=company)

    return render(request, 'core/company_dashboard/jobs/list_jobs.html', {
        'jobs': jobs
    })

#add job
@role_required(['company'])
def company_add_job(request):
    company = get_object_or_404(Company, user=request.user)

    if request.method == 'POST':
        Job.objects.create(
            company=company,
            job_title=request.POST.get('job_title'),
            job_type=request.POST.get('job_type'),
            location=request.POST.get('location'),
            status=request.POST.get('status'),
            min_salary=request.POST.get('min_salary') or None,
            max_salary=request.POST.get('max_salary') or None,
            description=request.POST.get('description')
        )

        return redirect('company_jobs_list')

    return render(request, 'core/company_dashboard/jobs/add_job.html')

#edit job
@role_required(['company'])
def company_edit_job(request, job_id):
    company = get_object_or_404(Company, user=request.user)
    job = get_object_or_404(Job, id=job_id, company=company)

    if request.method == 'POST':
        job.job_title = request.POST.get('job_title')
        job.job_type = request.POST.get('job_type')
        job.location = request.POST.get('location')
        job.status = request.POST.get('status')
        job.min_salary = request.POST.get('min_salary') or None
        job.max_salary = request.POST.get('max_salary') or None
        job.description = request.POST.get('description')
        job.save()

        return redirect('company_jobs_list')

    return render(request, 'core/company_dashboard/jobs/edit_job.html', {
        'job': job
    })
#show details
@role_required(['company'])
def company_job_details(request, job_id):
    company = get_object_or_404(Company, user=request.user)
    job = get_object_or_404(Job, id=job_id, company=company)

    return render(request, 'core/company_dashboard/jobs/job_details.html', {
        'job': job
    })

#delete job
@role_required(['company'])
def company_delete_job(request, job_id):
    company = get_object_or_404(Company, user=request.user)
    job = get_object_or_404(Job, id=job_id, company=company)

    if request.method == 'POST':
        job.delete()
        return redirect('company_jobs_list')

    return render(request, 'core/company_dashboard/jobs/delete_job.html', {
        'job': job
    })