from django.urls import path

from .views import (
    UserRegisterAPIView, 
    UserLoginAPIView,
    UserLoginAPIView
)

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name="register-user"),
    path('login/', UserLoginAPIView.as_view(), name="login"),
    path('logout/', UserLoginAPIView.as_view(), name="logout"),
]
