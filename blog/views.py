from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView

from .models import Blog

class BlogView(TemplateView):
    template_name = "blog.html"

    def blog_entries(self):
        paginator = Paginator(Blog.objects.filter(published=1).order_by("-publish_date"), 2)
        page = self.request.GET.get("page", None)
        try:
            blog_entries = paginator.page(page)
        except PageNotAnInteger:
            blog_entries = paginator.page(1)
        except EmptyPage:
            blog_entries = paginator.page(paginator.num_pages)
        return blog_entries

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context.update({"blog_entries": self.blog_entries})
        return context


class BlogEntryView(TemplateView):
    # TODO don't show draft posts
    template_name = "blog_detail.html"

    def blog_detail(self):
        return Blog.objects.get(pk=self.kwargs.get("pk", None))

    def prev_entry(self):
        try:
            return (Blog.objects
                .filter(publish_date__gt=self.blog_detail().publish_date)
                .filter(published=1)
                .order_by('-publish_date')[0])       
        except IndexError:
            return None 

    def next_entry(self):
        try:
            return (Blog.objects
                .filter(publish_date__lt=self.blog_detail().publish_date)
                .filter(published=1)
                .order_by('-publish_date')[0])
        except IndexError:
            return None

    def get_context_data(self, **kwargs):
        context = super(BlogEntryView, self).get_context_data(**kwargs)
        context.update({
            "blog": self.blog_detail(),
            "next_entry": self.next_entry(),
            "prev_entry": self.prev_entry()
            })
        return context