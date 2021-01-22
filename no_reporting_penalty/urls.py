from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.PenaltyTaxRateDetail.as_view()),
    path('', views.PenaltyTaxRateList.as_view()),

]