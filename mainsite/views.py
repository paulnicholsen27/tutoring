from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.template import Context
from forms import ContactForm

class HomepageView(TemplateView):
    template_name = "homepage.html"


class AboutView(TemplateView):
    template_name = "about.html"


class ContactView(TemplateView):
    template_name = "contact.html"

    form = ContactForm()
    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context.update({"form": self.form})
        return context

def contact_form(request):
    form_class = ContactForm
    if request.method == "POST":
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get("contact_name", "")
            contact_phone = request.POST.get("contact_phone", "")
            contact_email = request.POST.get("contact_email", "")
            content = request.POST.get("content", "")

            template = get_template("contact.txt")

            context = Context({
                "contact_name": contact_name,
                "contact_phone": contact_phone,
                "contact_email": contact_email,
                "content": content,
                })

            content = template.render(context)
            subject, from_email, to = "Within Reach Inquiry", contact_email, "pnichols104@gmail.com"
            email = EmailMessage(
                subject,
                content,
                from_email,
                ["pnichols104@gmail.com"],
                headers = {"Reply-To": contact_email}
                )
            email.send()
            return redirect("contact")
        else:
            print form.errors
            return redirect("about")
    else:
        return redirect("homepage")

