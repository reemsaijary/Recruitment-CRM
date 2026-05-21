from django.shortcuts import render, redirect, get_object_or_404
from core.models import Job, Company

# job list
def jobs_list(request):
    jobs = Job.objects.all()

    return render(request, 'core/jobs/list_jobs.html', {
        'jobs': jobs
    })

# add job
def add_job(request):
    companies = Company.objects.all()

    if request.method == 'POST':
        company = get_object_or_404(Company, id=request.POST.get('company'))

        Job.objects.create(
            company=company,
            job_title=request.POST.get('job_title'),
            location=request.POST.get('location'),
            required_skills=request.POST.get('required_skills'),
            status=request.POST.get('status'),
            job_type=request.POST.get('job_type'),
            salary_range=request.POST.get('salary_range'),
            description=request.POST.get('description')
        )

        return redirect('jobs_list')

    return render(request, 'core/jobs/add_job.html', {
        'companies': companies
    })

# view job details
def job_details(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    return render(request, 'core/jobs/job_details.html', {
        'job': job
    })

# edit job
def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    companies = Company.objects.all()

    if request.method == 'POST':
        company = get_object_or_404(Company, id=request.POST.get('company'))

        job.company = company
        job.job_title = request.POST.get('job_title')
        job.location = request.POST.get('location')
        job.required_skills = request.POST.get('required_skills')
        job.status = request.POST.get('status')
        job.job_type = request.POST.get('job_type')
        job.salary_range = request.POST.get('salary_range')
        job.description = request.POST.get('description')
        job.save()

        return redirect('jobs_list')

    return render(request, 'core/jobs/edit_job.html', {
        'job': job,
        'companies': companies
    })

# delete job
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        job.delete()
        return redirect('jobs_list')

    return render(request, 'core/jobs/delete_job.html', {
        'job': job
    })