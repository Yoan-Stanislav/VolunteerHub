from django.test import TestCase
from .models import Organization


class OrganizationTest(TestCase):
    def test_create_organization(self):
        org = Organization.objects.create(name="Test Org", description="desc")
        self.assertTrue(Organization.objects.filter(name="Test Org").exists())
