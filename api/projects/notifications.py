# notifications.py (create this utility file)

from django.core.mail import send_mail
from django.utils.timezone import now
from api.projects.models import Task
from django.conf import settings

def send_task_notification(task):
    subject = f"New Task Assigned: {task.title}"
    message = f"You have been assigned a new task: {task.title}.\n\nDescription: {task.description}\nDue Date: {task.due_date}"
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,  # Replace with your email
        [task.assigned_to.email],  # Assumes `assigned_to` is a field on Task model
    )

def send_due_date_notification(task):
    subject = f"Task Due Date Approaching: {task.title}"
    message = f"The task {task.title} is approaching its due date: {task.due_date}. Please complete it soon."
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,  # Replace with your email
        [task.assigned_to.email],  # Assumes `assigned_to` is a field on Task model
    )
