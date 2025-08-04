from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from events.models import Event
from organizations.models import Organization
from locations.models import Location


class EventCRUDTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="pass")
        self.organization = Organization.objects.create(name="Org", user=self.user)
        self.location = Location.objects.create(
            name="Test Location", address="Somewhere", city="Sofia"
        )

        self.event = Event.objects.create(
            title="Test Event",
            description="desc",
            date="2025-12-12",
            capacity=10,
            category="ENV",
            organization=self.organization,
            location=self.location,
        )
        self.client.login(username="testuser", password="pass")

    def test_event_dashboard(self):
        response = self.client.get(reverse("events:dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Event")

    def test_event_create(self):
        response = self.client.post(
            reverse("events:event-create"),
            {
                "title": "New Event",
                "description": "desc",
                "date": "2025-12-20",
                "capacity": 50,
                "category": "ENV",
                "organization": self.organization.id,
                "location": self.location.id,
            },
        )
        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertTrue(Event.objects.filter(title="New Event").exists())

    def test_event_update_permission(self):
        user2 = User.objects.create_user(username="other", password="pass")
        self.client.login(username="other", password="pass")
        url = reverse("events:event-update", args=[self.event.id])
        response = self.client.get(url)
        self.assertIn(
            response.status_code, [403, 302]
        )  # Forbidden or redirect to login

    def test_event_delete(self):
        url = reverse("events:event-delete", args=[self.event.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Event.objects.filter(pk=self.event.pk).exists())

    def test_event_create_invalid_capacity(self):
        response = self.client.post(
            reverse("events:event-create"),
            {
                "title": "Bad Event",
                "description": "desc",
                "date": "2025-12-20",
                "capacity": 0,  # INVALID!
                "category": "ENV",
                "organization": self.organization.id,
                "location": self.location.id,
            },
        )
        self.assertEqual(response.status_code, 200)  # Form re-renders with error
        self.assertFalse(Event.objects.filter(title="Bad Event").exists())
        self.assertContains(response, "Capacity must be at least 1.")

    def test_event_create_invalid_title(self):
        response = self.client.post(
            reverse("events:event-create"),
            {
                "title": "New",
                "description": "desc",
                "date": "2025-12-20",
                "capacity": 10,
                "category": "ENV",
                "organization": self.organization.id,
                "location": self.location.id,
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Event.objects.filter(title="New").exists())
        self.assertContains(response, "Title must be at least 5 characters.")

    def test_event_create_flash_message(self):
        response = self.client.post(
            reverse("events:event-create"),
            {
                "title": "Valid Title",
                "description": "desc",
                "date": "2025-12-21",
                "capacity": 11,
                "category": "ENV",
                "organization": self.organization.id,
                "location": self.location.id,
            },
            follow=True,
        )
        # Съобщението се намира в messages (виж base.html)
        self.assertContains(response, "Събитието беше създадено успешно!")
