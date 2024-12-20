from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RoleViewSet, UserProjectRoleViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'user-project-roles', UserProjectRoleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
