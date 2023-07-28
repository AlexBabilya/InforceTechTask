from rest_framework import routers

from modules.user.viewsets import UserViewSet
from modules.role.viewsets import RoleViewSet
from modules.employee.viewsets import EmployeeViewSet
from modules.auth.viewsets import (
    RegisterViewSet, 
    LoginViewSet, 
    RefreshViewSet,
    LogoutViewSet,
)

router = routers.SimpleRouter()

router.register(r'user', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r"auth/logout", LogoutViewSet, basename="auth-logout")
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
router.register(r'employee', EmployeeViewSet, basename='employee')

urlpatterns = [
    *router.urls,
]