from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('your-name/',views.get_name, name='your-name'),
    path('thanks/', views.index, name='index'),

    path('', views.login_home, name='login_home'),

    # path('usd/',views.usd, name='usd'),
    # path('index/', views.index, name='index'),

]


