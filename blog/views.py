from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView

from .models import Blog


class BlogView(TemplateView):
    template_name = "blog/blog.html"

    def blog_entries(self):
        entries_per_page = 5
        paginator = Paginator(Blog.objects
                              .filter(published=1)
                              .order_by("-publish_date"), entries_per_page)
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


class BlogDetailView(TemplateView):
    template_name = "blog/blog_detail.html"

    def blog_detail(self):
        return get_object_or_404(Blog, pk=self.kwargs.get("pk", None), published=1)

    def prev_entry(self):
        try:
            return (Blog.objects
                    .filter(publish_date__lt=self.blog_detail().publish_date)
                    .filter(published=1)
                    .order_by('-publish_date')[0])
        except IndexError:
            return None

    def next_entry(self):
        try:
            return (Blog.objects
                    .filter(publish_date__gt=self.blog_detail().publish_date)
                    .filter(published=1)
                    .order_by('publish_date')[0])
        except IndexError:
            return None

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context.update({
            "blog": self.blog_detail(),
            "next_entry": self.next_entry(),
            "prev_entry": self.prev_entry()
        })
        return context
