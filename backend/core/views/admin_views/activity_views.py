from django.shortcuts import render, redirect, get_object_or_404
from core.models import Activity, Application
from core.decorators import role_required

#list
@role_required(['admin'])
def activities_list(request):
    activities = Activity.objects.all()

    return render(request, 'core/admin_dashboard/activities/list_activities.html', {
        'activities': activities
    })

#add
@role_required(['admin'])
def add_activity(request):
    applications = Application.objects.all()

    if request.method == 'POST':
        application = get_object_or_404(Application, id=request.POST.get('application'))

        Activity.objects.create(
            application=application,
            activity_type=request.POST.get('activity_type'),
            due_date=request.POST.get('due_date'),
            status=request.POST.get('status'),
            notes=request.POST.get('notes')
        )

        return redirect('activities_list')

    return render(request, 'core/admin_dashboard/activities/add_activity.html', {
        'applications': applications,
        'status_choices': Activity.STATUS_CHOICES
    })

#details
@role_required(['admin'])
def activity_details(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)

    return render(request, 'core/admin_dashboard/activities/activity_details.html', {
        'activity': activity
    })

#edit
@role_required(['admin'])
def edit_activity(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    applications = Application.objects.all()

    if request.method == 'POST':
        activity.application = get_object_or_404(Application, id=request.POST.get('application'))
        activity.activity_type = request.POST.get('activity_type')
        activity.due_date = request.POST.get('due_date')
        activity.status = request.POST.get('status')
        activity.notes = request.POST.get('notes')
        activity.save()

        return redirect('activities_list')

    return render(request, 'core/admin_dashboard/activities/edit_activity.html', {
        'activity': activity,
        'applications': applications,
        'status_choices': Activity.STATUS_CHOICES
    })

#delete
@role_required(['admin'])
def delete_activity(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)

    if request.method == 'POST':
        activity.delete()
        return redirect('activities_list')

    return render(request, 'core/admin_dashboard/activities/delete_activity.html', {
        'activity': activity
    })