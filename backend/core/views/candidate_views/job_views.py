from django.shortcuts import render, get_object_or_404, redirect
from core.models import Candidate, Job, Application
from core.decorators import role_required

#job list
@role_required(['candidate'])
def candidate_jobs_list(request):
    jobs = Job.objects.filter(status='Open')

    return render(request, 'core/candidate_dashboard/jobs/list_jobs.html', {
        'jobs': jobs
    })

#job details
@role_required(['candidate'])
def candidate_job_details(request, job_id):
    job = get_object_or_404(Job, id=job_id, status='Open')

    return render(request, 'core/candidate_dashboard/jobs/job_details.html', {
        'job': job
    })

#apply to job
@role_required(['candidate'])
def apply_to_job(request, job_id):
    candidate = get_object_or_404(Candidate, user=request.user)
    job = get_object_or_404(Job, id=job_id, status='Open')

    existing_application = Application.objects.filter(
        candidate=candidate,
        job=job
    ).first()

    if existing_application:
        return redirect('candidate_applications_list')

    Application.objects.create(
        candidate=candidate,
        job=job,
        status='Applied',
        notes='Applied by candidate'
    )

    return redirect('candidate_applications_list')