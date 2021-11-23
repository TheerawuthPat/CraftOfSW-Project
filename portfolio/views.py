from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy # new
from .models import Contact

class HomePageView(TemplateView):
    model = Contact
    template_name = 'home.html'

class OverViewPageView(TemplateView):
    model = Contact
    template_name = 'blogs/overview.html'

class UxDesignPageView(TemplateView):
    model = Contact
    template_name = 'blogs/ux-design.html'

class UiDesignPageView(TemplateView):
    model = Contact
    template_name = 'blogs/ui-design.html'

class ResearchPageView(TemplateView):
    model = Contact
    template_name = 'blogs/research.html'

class AboutPageView(TemplateView):
    model = Contact
    template_name = 'blogs/about.html'

class ContactPageView(CreateView):
    model = Contact
    template_name = 'blogs/contact.html'
    success_url = reverse_lazy('home')
    fields = ['firstname', 'lastname', 'email', 'phone']

class ContactListPageView(TemplateView):
    model = Contact
    template_name = 'blogs/contact-list.html'
    fields = ['firstname', 'lastname', 'email', 'phone']
    