from django.urls import path

from .views import MenuUploadAPIView, CurrentDayMenuList

urlpatterns = [
    path('', CurrentDayMenuList.as_view(), name='menu_list'),
    path('upload/', MenuUploadAPIView.as_view(), name='menu_upload'),
]