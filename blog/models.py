from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

from ckeditor_uploader.fields import RichTextUploadingField


class Blog(models.Model):

    PUBLISH_CHOICES = ((1, "Published"),
                       (2, "Draft")
                       )

    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    opening_content = RichTextUploadingField()
    extended_content = RichTextUploadingField(blank=True, null=True)
    published = models.IntegerField(choices=PUBLISH_CHOICES, default=2)
    publish_date = models.DateTimeField(db_index=True, auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def full_content(self):
        return self.opening_content + self.extended_content

    def get_absolute_url(self):
        return reverse("blog:blog_entry", kwargs={"slug": self.slug, "pk": self.pk})
