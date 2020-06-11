from django.core.mail import send_mail
from django import forms
import logging

logger = logging.getLogger(__name__)


class ContactForm(forms.Form):
    name = forms.CharField(label=' Su nombre',
                           max_length=100)
    message = forms.CharField(label="Mensaje",
                              max_length=300,
                              widget=forms.Textarea)

    def send_mail(self):
        logger.info("Enviando eMail al servicio al cliente")
        message = "Desde: {}\n{}".format(self.cleaned_data['name'],
                                         self.cleaned_data['message']
                                         )
        send_mail("Mensaje desde Web",
                  message,
                  "my.site@domain.com",
                  ['cm.1@domain.co', 'cm.2@domain.co'],
                  fail_silently=False)
