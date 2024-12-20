from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserProjectRole(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'project', 'role')
