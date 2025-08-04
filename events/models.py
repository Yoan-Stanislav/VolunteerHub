from datetime import date
from django.core.exceptions import ValidationError
from django.db import models
from organizations.models import Organization
from locations.models import Location


def validate_future(value):
    if value < date.today():
        raise ValidationError("Date must be in the future.")


class Event(models.Model):
    CATEGORY = [
        ("ENV", "Environment"),
        ("SOC", "Social"),
        ("EDU", "Education"),
        ("HEA", "Health"),
        ("ART", "Art & Culture"),
    ]

    title = models.CharField(max_length=80)
    description = models.TextField()
    date = models.DateField(validators=[validate_future])
    capacity = models.PositiveIntegerField()
    category = models.CharField(max_length=3, choices=CATEGORY)
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="events"
    )
    location = models.ForeignKey(
        Location, on_delete=models.PROTECT, related_name="events"
    )

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.title} ({self.date})"

    @property
    def available_seats(self):
        return self.capacity - self.applications.filter(status="APP").count()
