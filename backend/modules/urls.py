from .role.views import RoleListAPIView
from .employee.views import CreateEmployeeAPIView
from django.urls import path, include

urlpatterns = [
    path('auth/', include('modules.auth.urls'), name='auth'),
    path('restaurant/', include('modules.restaurant.urls'), name='restaurant'),
    path('menu/', include('modules.menu.urls'), name='menu'),
    path('vote/', include('modules.vote.urls'), name='vote'),
    path('roles/', RoleListAPIView.as_view(), name="roles"),
    path('employees/', CreateEmployeeAPIView.as_view(), name="employees"),
]