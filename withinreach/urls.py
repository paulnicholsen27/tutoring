from django.conf.urls import url
from django.contrib import admin
from mainsite.views import (HomepageView, BlogView,
                            BlogEntryView, AboutView, ContactView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomepageView.as_view()),
    url(r'^blog/', BlogView.as_view()),
    # url(r'^blog/{{pk}}/', BlogEntryView.as_view()),
    url(r'^about/', AboutView.as_view()),
    url(r'^contact/', ContactView.as_view()),
]
