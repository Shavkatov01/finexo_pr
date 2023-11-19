from django import urls
from django.urls import path
from finexo import views


urlpatterns = [
    path('home/', views.HomeList.as_view(), name='home'),
    path('about/', views.AboutList.as_view(), name='about'),
    path('service/', views.ServiceList.as_view(), name='service'),
    path('why/', views.WhyChooseList.as_view(), name='why'),
    path('team/', views.TeamList.as_view(), name='team'),
    path('customer/', views.CustomerList.as_view(), name='customer'),
    
]