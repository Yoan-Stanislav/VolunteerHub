from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from events.models import Event
from organizations.models import Organization
from locations.models import Location
from applications.models import Application

class ApplicationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.organization = Organization.objects.create(name='Org', user=self.user)
        self.location = Location.objects.create(name='AppTest Location', address='N/A', city='Plovdiv')
        self.event = Event.objects.create(
            title='Ev', description='desc', date='2025-11-11',
            capacity=15, category='ENV',
            organization=self.organization,
            location=self.location,
        )
        self.client.login(username='testuser', password='pass')

    def test_application_create(self):
        url = reverse('applications:application-create', args=[self.event.pk])
        response = self.client.post(url, {'message': 'Can I join?'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Application.objects.filter(user=self.user, event=self.event).exists())
