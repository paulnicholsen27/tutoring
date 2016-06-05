from django.conf.urls import url
from django.contrib import admin
from .views import BlogView, BlogDetailView

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/(?P<pk>\d+)/', BlogDetailView.as_view(), name="blog_detail"),
    url(r'^$', BlogView.as_view(), name="blog"),
]
