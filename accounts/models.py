from django.contrib.auth.models import User
from django.db import models

class VolunteerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=15, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    skills = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="profile_images/",
        blank=True,
        null=True,
        default="profile_images/default.png"
    )

    def save(self, *args, **kwargs):
        # Ако снимката е None или празна, слагаме default
        if not self.image:
            self.image = "profile_images/default.png"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    subject = models.CharField(max_length=120)
    body = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"From {self.sender} to {self.recipient} - {self.subject}"
