from django.test import TestCase
from django.urls import reverse
from main import forms


class TestPage(TestCase):
    def test_home_page_works(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'main')

    def test_about_us_page_works(self):
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_us.html')
        self.assertContains(response, 'main')

    def test_contact_us_works(self):
        response = self.client.get(reverse("contact_us"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact_us.html")
        self.assertContains(response, 'main')
        self.assertIsInstance(response.context['form'], forms.ContactForm)
