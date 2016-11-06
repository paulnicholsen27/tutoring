from django.core.urlresolvers import reverse
from django.test import TestCase, Client


class TestPageLoads(TestCase):

    def setUp(self):
        self.client = Client()

    def test_homepage_load(self):
        homepage_url = reverse("homepage")
        r = self.client.get(homepage_url)
        self.assertEqual(r.status_code, 200)

    def test_about_load(self):
        about_url = reverse("about")
        r = self.client.get(about_url)
        self.assertEqual(r.status_code, 200)

    def test_contact_load(self):
        contact_url = reverse("contact")
        r = self.client.get(contact_url)
        self.assertEqual(r.status_code, 200)
