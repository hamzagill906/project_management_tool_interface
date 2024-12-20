from django.db import models
from api.users.models import User, UserProjectRole


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    team_members = models.ManyToManyField(User, through=UserProjectRole)

    def __str__(self):
        return self.title


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low')
    ]
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    due_date = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    dependencies = models.ManyToManyField('self', symmetrical=False)

    def __str__(self):
        return self.title
