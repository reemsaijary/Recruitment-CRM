from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from core.models import Candidate, Job, Application, Notification
from core.decorators import role_required
from django.urls import reverse

# job list
@role_required(['candidate'])
def candidate_jobs_list(request):
    candidate = get_object_or_404(Candidate, user=request.user)

    jobs = Job.objects.filter(status='Open').select_related('company').order_by('-created_at')

    search = request.GET.get('search', '')
    job_type = request.GET.get('job_type', '')
    location = request.GET.get('location', '')

    if search:
        jobs = jobs.filter(
            Q(job_title__icontains=search) |
            Q(company__company_name__icontains=search) |
            Q(description__icontains=search)
        )

    if job_type:
        jobs = jobs.filter(job_type__icontains=job_type)

    if location:
        jobs = jobs.filter(location__icontains=location)

    applied_job_ids = Application.objects.filter(
        candidate=candidate
    ).values_list('job_id', flat=True)

    total_open_jobs = Job.objects.filter(status='Open').count()
    remote_jobs = Job.objects.filter(status='Open', job_type__icontains='Remote').count()
    applied_jobs = Application.objects.filter(candidate=candidate).count()

    paginator = Paginator(jobs, 6)
    page_number = request.GET.get('page')
    jobs = paginator.get_page(page_number)

    return render(request, 'core/candidate_dashboard/jobs/list_jobs.html', {
        'jobs': jobs,
        'search': search,
        'job_type': job_type,
        'location': location,
        'applied_job_ids': applied_job_ids,
        'total_open_jobs': total_open_jobs,
        'remote_jobs': remote_jobs,
        'applied_jobs': applied_jobs,
    })


# job details
@role_required(['candidate'])
def candidate_job_details(request, job_id):
    candidate = get_object_or_404(Candidate, user=request.user)
    job = get_object_or_404(Job, id=job_id, status='Open')

    already_applied = Application.objects.filter(
        candidate=candidate,
        job=job
    ).exists()

    return render(request, 'core/candidate_dashboard/jobs/job_details.html', {
        'job': job,
        'already_applied': already_applied,
    })


# apply to job
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

    application = Application.objects.create(
        candidate=candidate,
        job=job,
        status='Applied',
        notes='Applied by candidate'
    )

    if job.company.user:
        Notification.objects.create(
            user=job.company.user,
            title='New Application Received',
            message=f'{candidate.full_name} applied for {job.job_title}.',
            url=reverse('company_application_details', args=[application.id]),
            notification_type='application'
    )
    return redirect('candidate_applications_list')