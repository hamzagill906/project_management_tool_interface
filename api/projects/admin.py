from django.contrib import admin
from .models import Project, Task
from api.users.models import UserProjectRole


class UserProjectRoleInline(admin.TabularInline):
    model = UserProjectRole
    extra = 1
    autocomplete_fields = ['user', 'role']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    search_fields = ('title', 'description')
    inlines = [UserProjectRoleInline]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'priority', 'status', 'due_date')
    list_filter = ('priority', 'status', 'project')
    search_fields = ('title', 'description')
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'dependencies':
            # Filter tasks by the project the task belongs to
            task_id = request.GET.get('task')
            task = Task.objects.get(id=task_id) if task_id else None
            if task:
                kwargs['queryset'] = Task.objects.filter(project=task.project)
        return super().formfield_for_manytomany(db_field, request, **kwargs)
