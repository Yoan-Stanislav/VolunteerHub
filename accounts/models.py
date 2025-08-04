from django.contrib.auth.models import User
from django.db import models


class VolunteerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=15, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    skills = models.TextField(blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username
