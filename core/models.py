from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Име")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Съобщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата/Час")
    is_answered = models.BooleanField(default=False, verbose_name="Отговорено")
    reply = models.TextField(blank=True, null=True, verbose_name="Отговор от админ")

    def __str__(self):
        return f"{self.name} - {self.email} ({self.created_at:%d.%m.%Y %H:%M})"
