# management/commands/send_due_date_notifications.py

from django.core.management.base import BaseCommand
from django.utils.timezone import now, timedelta
from api.projects.models import Task
from api.projects.notifications import send_due_date_notification

class Command(BaseCommand):
    help = 'Send due date notifications for tasks that are approaching their due date.'

    def handle(self, *args, **kwargs):
        approaching_due_date = now() + timedelta(days=2)
        tasks = Task.objects.filter(due_date__lte=approaching_due_date, status='in_progress')

        for task in tasks:
            send_due_date_notification(task)

        self.stdout.write(self.style.SUCCESS(f'Successfully sent notifications for {tasks.count()} tasks.'))
