from django.conf.urls import url
from django.contrib import admin
from mainsite.views import (HomepageView, BlogView,
                            BlogEntryView, AboutView, ContactView)

urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^$', HomepageView.as_view(), name="homepage"),
    url(r'^blog/(?P<slug>[-\w]+)/(?P<pk>\d+)/', BlogEntryView.as_view(), name="blog_entry"),
    url(r'^blog/', BlogView.as_view(), name="blog"),
    url(r'^about/', AboutView.as_view(), name="about"),
    url(r'^contact/', ContactView.as_view(), name="contact"),
]
