from django.urls import path
from . import views

urlpatterns = [
    # path('your-name/',views.get_name, name='your-name'),
    # path('thanks/', views.index, name='index'),

    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('no_reporting/', views.no_reporting, name='no_reporting'),


]


