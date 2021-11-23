from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class OverViewPageView(TemplateView):
    template_name = 'blogs/overview.html'

class UxDesignPageView(TemplateView):
    template_name = 'blogs/ux-design.html'

class UiDesignPageView(TemplateView):
    template_name = 'blogs/ui-design.html'

class ResearchPageView(TemplateView):
    template_name = 'blogs/research.html'

class AboutPageView(TemplateView):
    template_name = 'blogs/about.html'

class ContactPageView(TemplateView):
    template_name = 'blogs/contact.html'

class ContactListPageView(TemplateView):
    template_name = 'blogs/contact-list.html'
    