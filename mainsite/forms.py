from django import forms
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.template import Context

# from captcha.fields import CaptchaField


class ContactForm(forms.Form):

    contact_name = forms.CharField()
    contact_email = forms.EmailField()
    contact_phone = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    cc_me = forms.BooleanField(required=False, initial=False)
    # captcha = CaptchaField(required=True)

    def send_email(self):
        contact_name = self.data["contact_name"]
        contact_phone = self.data["contact_phone"]
        contact_email = self.data["contact_email"]
        content = self.data["content"]

        template = get_template("contact.txt")

        context = Context({
            "contact_name": contact_name,
            "contact_phone": contact_phone,
            "contact_email": contact_email,
            "content": content,
        })

        content = template.render(context)
        subject, from_email, to = "Within Reach Inquiry", contact_email, "jason@withinreachgroup.com"
        cc_address = contact_email if "cc_me" in self.data else None
        email = EmailMultiAlternatives(
            subject,
            content,
            from_email,
            ["jason@withinreachgroup.com"],
            cc=[cc_address],
            headers={"Reply-To": contact_email}
        )
        email.send()

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
