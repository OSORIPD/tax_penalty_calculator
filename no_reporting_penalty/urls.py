from django.urls import path
from . import views

urlpatterns = [
    path('', views.no_reporting, name='no_reporting'),
    path('no_reporting/', views.no_reporting, name='no_reporting'),


]


