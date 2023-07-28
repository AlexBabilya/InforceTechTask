from django.urls import path

from .views import RestaurantListAPIView, RestaurantCreateAPIView

urlpatterns = [
    path('', RestaurantListAPIView.as_view(), name='restaurants_list'),
    path('create/', RestaurantCreateAPIView.as_view(), name='restaurants_create'),
]