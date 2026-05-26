from django.shortcuts import render, redirect, get_object_or_404
from core.models import Company, Application, Interview
from core.decorators import role_required

#list 
@role_required(['company'])
def company_interviews_list(request):
    company = get_object_or_404(Company, user=request.user)

    interviews = Interview.objects.filter(
        application__job__company=company
    ).select_related('application', 'application__candidate', 'application__job')

    return render(request, 'core/company_dashboard/interviews/list_interviews.html', {
        'interviews': interviews
    })

#add
@role_required(['company'])
def company_add_interview(request, application_id):
    company = get_object_or_404(Company, user=request.user)

    application = get_object_or_404(
        Application,
        id=application_id,
        job__company=company
    )

    if request.method == "POST":
        Interview.objects.create(
            application=application,
            interview_date=request.POST.get('interview_date'),
            interview_type=request.POST.get('interview_type'),
            status=request.POST.get('status'),
            notes=request.POST.get('notes')
        )

        application.status = "Interview Scheduled"
        application.save()

        return redirect('company_interviews_list')

    return render(request, 'core/company_dashboard/interviews/add_interview.html', {
        'application': application,
        'status_choices': Interview.STATUS_CHOICES
    })

#show details
@role_required(['company'])
def company_interview_details(request, interview_id):
    company = get_object_or_404(Company, user=request.user)

    interview = get_object_or_404(
        Interview,
        id=interview_id,
        application__job__company=company
    )

    return render(request, 'core/company_dashboard/interviews/interview_details.html', {
        'interview': interview
    })

#edit 
@role_required(['company'])
def company_edit_interview(request, interview_id):
    company = get_object_or_404(Company, user=request.user)

    interview = get_object_or_404(
        Interview,
        id=interview_id,
        application__job__company=company
    )

    if request.method == "POST":
        interview.interview_date = request.POST.get('interview_date')
        interview.interview_type = request.POST.get('interview_type')
        interview.status = request.POST.get('status')
        interview.notes = request.POST.get('notes')
        interview.save()

        return redirect('company_interview_details', interview_id=interview.id)

    return render(request, 'core/company_dashboard/interviews/edit_interview.html', {
        'interview': interview,
        'status_choices': Interview.STATUS_CHOICES
    })

#delete
@role_required(['company'])
def company_delete_interview(request, interview_id):
    company = get_object_or_404(Company, user=request.user)

    interview = get_object_or_404(
        Interview,
        id=interview_id,
        application__job__company=company
    )

    if request.method == "POST":
        interview.delete()
        return redirect('company_interviews_list')

    return render(request, 'core/company_dashboard/interviews/delete_interview.html', {
        'interview': interview
    })