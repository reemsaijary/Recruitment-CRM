from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from core.models import Notification


@login_required
def notifications_list(request):
    notifications = Notification.objects.filter(
        user=request.user
    ).order_by('-created_at')

    unread_notifications_count = notifications.filter(is_read=False).count()

    role = request.user.profile.role

    if role == 'company':
        template = 'core/notifications/list_notifications_company.html'
    else:
        template = 'core/notifications/list_notifications_candidate.html'

    return render(request, template, {
        'notifications': notifications,
        'unread_notifications_count': unread_notifications_count,
    })


@login_required
def mark_notification_read(request, notification_id):
    notification = get_object_or_404(
        Notification,
        id=notification_id,
        user=request.user
    )

    notification.is_read = True
    notification.save()

    if notification.url:
        return redirect(notification.url)

    return redirect('notifications_list')

@login_required
def mark_all_notifications_read(request):
    Notification.objects.filter(
        user=request.user,
        is_read=False
    ).update(is_read=True)

    return redirect('notifications_list')