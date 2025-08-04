from django.test import TestCase
from django.urls import reverse


class ContactTest(TestCase):
    def test_contact_form(self):
        response = self.client.post(
            reverse("contact:contact"),
            {
                "name": "Ivan",
                "email": "ivan@example.com",
                "message": "This is a long enough message!",
            },
        )
        self.assertEqual(response.status_code, 302)  # Success redirects
