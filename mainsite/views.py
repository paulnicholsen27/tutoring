import os

from django.contrib import messages
from django.shortcuts import render, redirect
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
    form_class = ContactForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.send_email()
            messages.add_message(request, messages.INFO, "Your email has been sent.  We will respond within 48 hours.  If this is an emergency please call 911.")
            return redirect('contact')
        else:
            print form.errors
            messages.add_message(request, messages.ERROR, "Please correct the errors below.")
            return redirect('contact')
        return render(request, self.template_name, {'form': form})

    # def get_context_data(self, **kwargs):
    #     context = super(ContactView, self).get_context_data(**kwargs)
    #     print GOOGLE_API_KEY
    #     context.update({"form": self.form_class, "google_api": GOOGLE_API_KEY})
    #     return context
