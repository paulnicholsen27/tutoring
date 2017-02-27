from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.utils.text import slugify

from ckeditor_uploader.fields import RichTextUploadingField


class Blog(models.Model):

    PUBLISH_CHOICES = ((1, "Published"),
                       (2, "Draft")
                       )

    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    opening_content = RichTextUploadingField(help_text="Teaser text to appear on main blog page")
    extended_content = RichTextUploadingField(blank=True, null=True,
                                              help_text="Remainder of text to appear on detail page of entry (optional)")
    published = models.IntegerField(choices=PUBLISH_CHOICES, default=2,
                                    help_text="Set to 'Published' when post is ready to appear to public")
    publish_date = models.DateTimeField(db_index=True, auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def full_content(self):
        if self.extended_content:
            return self.opening_content + self.extended_content
        else:
            return self.opening_content

    def get_absolute_url(self):
        return reverse("blog:blog_detail", kwargs={"slug": self.slug, "pk": self.pk})

    def get_full_absolute_url(self):
        domain = Site.objects.get_current().domain

        return "http://%s%s" % (domain, self.get_absolute_url())

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)
