# tasks.py (Celery task)

from celery import shared_task
from django.utils.timezone import now, timedelta
from api.projects.models import Task
from api.projects.notifications import send_due_date_notification

@shared_task
def check_due_dates():
    approaching_due_date = now() + timedelta(days=2)
    tasks = Task.objects.filter(due_date__lte=approaching_due_date, status='in_progress')

    for task in tasks:
        send_due_date_notification(task)
