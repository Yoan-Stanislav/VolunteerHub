from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class AccountsTest(TestCase):
    def test_register(self):
        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "reguser",
                "email": "reg@test.bg",
                "password1": "S0mePass!word",
                "password2": "S0mePass!word",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="reguser").exists())

    def test_login(self):
        User.objects.create_user(username="t", password="pass")
        response = self.client.post(
            reverse("accounts:login"), {"username": "t", "password": "pass"}
        )
        self.assertEqual(response.status_code, 302)
