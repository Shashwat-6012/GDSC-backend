
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home, name = 'Home page'),
    path('test', views.test, name = 'tester'),
    path('Evdisplay', views.displaypage, name = "display"),
    path('eventform', views.eventform, name = "event form handle")
]