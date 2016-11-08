from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from .models import Blog


class TestPageLoads(TestCase):

    def setUp(self):
        self.client = Client()
        self.published_blog = Blog(
            title="published",
            opening_content="blah blah",
        )
        self.published_blog.save()

    def test_blog_main_load(self):
        blog_main_url = reverse("blog:blog")
        r = self.client.get(blog_main_url)
        self.assertEqual(r.status_code, 200)

    def test_blog_detail_load(self):
        blog_detail_url = reverse("blog:blog_detail",
                                  kwargs={"slug": self.published_blog.slug,
                                          "pk": self.published_blog.pk})
        r = self.client.get(blog_detail_url)
        self.assertEqual(r.status_code, 200)
