from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Blog


class HomepageView(TemplateView):
    template_name = "homepage.html"


class BlogView(TemplateView):
    template_name = "blog.html"

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        blog_entries = Blog.objects.filter(published=1).order_by("-publish_date")
        context.update({"blog_entries": blog_entries})
        return context


class BlogEntryView(TemplateView):
    template_name = "blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super(BlogEntryView, self).get_context_data(**kwargs)
        blog = Blog.objects.get(pk=self.kwargs.get("pk", None))
        context.update({"blog": blog})
        return context

class AboutView(TemplateView):
    template_name = "about.html"


class ContactView(TemplateView):
    template_name = "contact.html"
