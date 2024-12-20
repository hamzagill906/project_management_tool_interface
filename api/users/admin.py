from django.contrib import admin
from .models import User, Role, UserProjectRole

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff')
    search_fields = ('username', 'email')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(UserProjectRole)
class UserProjectRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'role')
    list_filter = ('role',)
    search_fields = ('user__username', 'project__title', 'role__name')
