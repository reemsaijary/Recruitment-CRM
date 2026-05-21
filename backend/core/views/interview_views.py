from django.shortcuts import render, redirect, get_object_or_404
from core.models import Interview, Application

# show interview list
def interviews_list(request):
    interviews = Interview.objects.all()

    return render(request, 'core/interviews/list_interviews.html', {
        'interviews': interviews
    })

# add interview
def add_interview(request):
    applications = Application.objects.all()

    if request.method == 'POST':
        application = get_object_or_404(Application, id=request.POST.get('application'))

        Interview.objects.create(
            application=application,
            interview_date=request.POST.get('interview_date'),
            interview_type=request.POST.get('interview_type'),
            status=request.POST.get('status'),
            notes=request.POST.get('notes')
        )

        return redirect('interviews_list')

    return render(request, 'core/interviews/add_interview.html', {
        'applications': applications,
        'status_choices': Interview.STATUS_CHOICES
    })

# view details
def interview_details(request, interview_id):
    interview = get_object_or_404(Interview, id=interview_id)

    return render(request, 'core/interviews/interview_details.html', {
        'interview': interview
    })

#edit details
def edit_interview(request, interview_id):
    interview = get_object_or_404(Interview, id=interview_id)
    applications = Application.objects.all()

    if request.method == 'POST':
        interview.application = get_object_or_404(Application, id=request.POST.get('application'))
        interview.interview_date = request.POST.get('interview_date')
        interview.interview_type = request.POST.get('interview_type')
        interview.status = request.POST.get('status')
        interview.notes = request.POST.get('notes')
        interview.save()

        return redirect('interviews_list')

    return render(request, 'core/interviews/edit_interview.html', {
        'interview': interview,
        'applications': applications,
        'status_choices': Interview.STATUS_CHOICES
    })

#delete interview
def delete_interview(request, interview_id):
    interview = get_object_or_404(Interview, id=interview_id)

    if request.method == 'POST':
        interview.delete()
        return redirect('interviews_list')

    return render(request, 'core/interviews/delete_interview.html', {
        'interview': interview
    })