from django.urls import path

from .views import (
    UserRegisterAPIView, 
    UserLoginAPIView,
    UserLogoutView
)

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name="register-user"),
    path('login/', UserLoginAPIView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
]
