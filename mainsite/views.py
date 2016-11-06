from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView

from forms import ContactForm
from common.tokens_and_keys import GOOGLE_API_KEY


class HomepageView(TemplateView):
    template_name = "homepage.html"


class AboutView(TemplateView):
    template_name = "about.html"


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
            return redirect('contact')
        return render(request, self.template_name, {'form': form})

    # def get_context_data(self, **kwargs):
    #     context = super(ContactView, self).get_context_data(**kwargs)
    #     print GOOGLE_API_KEY
    #     context.update({"form": self.form_class, "google_api": GOOGLE_API_KEY})
    #     return context
