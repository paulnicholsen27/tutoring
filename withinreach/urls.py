from django.conf.urls import url, include
from django.contrib import admin
from mainsite.views import HomepageView, AboutView, ContactView

urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^$', HomepageView.as_view(), name="homepage"),
    url(r'^about/', AboutView.as_view(), name="about"),
    url(r'^contact/', ContactView.as_view(), name="contact"),
    url(r'^blog/', include("blog.urls", namespace="blog")),
]
