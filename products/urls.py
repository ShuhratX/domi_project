from turtle import home
from django.urls import path
from .views import home_view, phone_view

urlpatterns = [
    path('', home_view),
    path('phone', phone_view, name = 'phone'),
]
