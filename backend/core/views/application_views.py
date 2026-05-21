from django.shortcuts import render, redirect, get_object_or_404
from core.models import Application, Candidate, Job

# application list
def applications_list(request):
    applications = Application.objects.all()

    return render(request, 'core/applications/list_applications.html', {
        'applications': applications
    })

# add
def add_application(request):
    candidates = Candidate.objects.all()
    jobs = Job.objects.all()

    if request.method == 'POST':
        candidate = get_object_or_404(Candidate, id=request.POST.get('candidate'))
        job = get_object_or_404(Job, id=request.POST.get('job'))

        Application.objects.create(
            candidate=candidate,
            job=job,
            status=request.POST.get('status'),
            notes=request.POST.get('notes')
        )

        return redirect('applications_list')

    return render(request, 'core/applications/add_application.html', {
        'candidates': candidates,
        'jobs': jobs,
        'status_choices': Application.STATUS_CHOICES
    })

# show details
def application_details(request, application_id):
    application = get_object_or_404(Application, id=application_id)

    return render(request, 'core/applications/application_details.html', {
        'application': application
    })

# edit data
def edit_application(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    candidates = Candidate.objects.all()
    jobs = Job.objects.all()

    if request.method == 'POST':
        application.candidate = get_object_or_404(Candidate, id=request.POST.get('candidate'))
        application.job = get_object_or_404(Job, id=request.POST.get('job'))
        application.status = request.POST.get('status')
        application.notes = request.POST.get('notes')
        application.save()

        return redirect('applications_list')

    return render(request, 'core/applications/edit_application.html', {
        'application': application,
        'candidates': candidates,
        'jobs': jobs,
        'status_choices': Application.STATUS_CHOICES
    })

# delete data
def delete_application(request, application_id):
    application = get_object_or_404(Application, id=application_id)

    if request.method == 'POST':
        application.delete()
        return redirect('applications_list')

    return render(request, 'core/applications/delete_application.html', {
        'application': application
    })