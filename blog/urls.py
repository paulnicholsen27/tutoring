from django.conf.urls import url
from django.contrib import admin
from .views import BlogView, BlogEntryView

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/(?P<pk>\d+)/', BlogEntryView.as_view(), name="blog_entry"),
    url(r'^$', BlogView.as_view(), name="blog"),
]
