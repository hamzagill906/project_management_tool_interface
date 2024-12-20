from django.db import models
from api.projects.models import Task
from api.users.models import User

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications', null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.recipient.email} regarding {self.task.title}"
