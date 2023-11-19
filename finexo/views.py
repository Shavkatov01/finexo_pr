from django.shortcuts import render
from .models import Home, About, Service, WhyChoose, Customer, Team
from django.views.generic import ListView


class HomeList(ListView):
    model = Home
    template_name = 'home.html'


class AboutList(ListView):
    model = About
    template_name = 'about.html'

class ServiceList(ListView):
    model = Service
    template_name = 'service.html'


class WhyChooseList(ListView):
    model = WhyChoose
    template_name = 'why.html'


class CustomerList(ListView):
    model = Customer
    template_name = 'customer.html'

class TeamList(ListView):
    model = Team
    template_name = 'team.html'

    