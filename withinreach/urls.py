from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from mainsite.views import HomepageView, AboutView, ContactView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^$', HomepageView.as_view(), name="homepage"),
    url(r'^about/', AboutView.as_view(), name="about"),
    url(r'^contact/', ContactView.as_view(), name="contact"),
    # url(r'^contact-form/', contact_form, name="contact-form"),
    url(r'^blog/', include("blog.urls", namespace="blog")),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
            }
        ),
    ]

urlpatterns += staticfiles_urlpatterns()