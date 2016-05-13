from django.shortcuts import render
from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = "homepage.html"


class BlogView(TemplateView):
    template_name = "blog.html"


class AboutView(TemplateView):
    template_name = "about.html"


class ContactView(TemplateView):
    template_name = "contact.html"
