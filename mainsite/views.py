import os

from django.contrib import messages
from django.shortcuts import render, redirect, render_to_response
from django.views.generic import TemplateView, FormView
from forms import ContactForm


try:
    from common.tokens_and_keys import GOOGLE_API_KEY
except ImportError:
    GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]


class HomepageView(TemplateView):
    template_name = "homepage.html"


class AboutView(TemplateView):
    template_name = "about.html"


class PaymentView(TemplateView):
    template_name = "payment.html"


class ContactView(FormView):
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        form = ContactForm(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            messages.add_message(request, messages.INFO, "Your email has been sent.  We will respond within 48 hours.  If this is an emergency please call 911.")
            return redirect('contact')
        else:
            messages.add_message(request, messages.ERROR, "Please correct the errors below.")
            return render(request, self.template_name, {'form': form})
