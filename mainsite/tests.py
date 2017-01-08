import sys

from django.core import mail
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

    def test_payment_load(self):
        payment_url = reverse("payment")
        r = self.client.get(payment_url)
        self.assertEqual(r.status_code, 200)


class TestContactEmail(TestCase):

    def setUp(self):
        self.client = Client()

    def test_email_sent(self):
        post_data = {}
        post_data["contact_name"] = "Joey McEmailHead"
        post_data["contact_email"] = "joey@email.com"
        post_data["contact_phone"] = "2015551212"
        post_data["content"] = "Blah blah"
        post_data['captcha_0'] = 'dummy-value'
        post_data['captcha_1'] = 'PASSED'
        contact_url = reverse("contact")
        r = self.client.post(contact_url, data=post_data)
        self.assertEquals(mail.outbox[0].subject, 'Within Reach Inquiry')
