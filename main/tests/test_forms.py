from django.test import TestCase
from django.core import mail
from main import forms


class TestForm(TestCase):

    def test_valid_contact_us_send_email(self):
        form = forms.ContactForm({
            'name': ' Kevin Herney',
            'message': 'Hi there'
        })

        self.assertTrue(form.is_valid())

        with self.assertLogs('main.forms', level='INFO') as cm:
            form.send_mail()
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Mensaje desde Web')
        self.assertGreaterEqual(len(cm.output), 1)

    def test_invalid_contact_us_form(self):
        form = forms.ContactForm({
            'messahe': 'Hi there'
        })
        self.assertFalse(form.is_valid())
