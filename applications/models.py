from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

class Application(models.Model):
    STATUS_CHOICES = (
        ("PEN", "Pending"),
        ("APP", "Approved"),
        ("REJ", "Rejected"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="applications",
    )
    event = models.ForeignKey(
        "events.Event",              # <= важнo: стрингова FK
        on_delete=models.CASCADE,
        related_name="applications",
    )
    message = models.TextField(blank=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default="PEN")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "event")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} -> {self.event} [{self.get_status_display()}]"

    def clean(self):
        if getattr(self, "event_id", None) and self.event.date < timezone.localdate():
            raise ValidationError("Събитието вече е минало.")
        return super().clean()
