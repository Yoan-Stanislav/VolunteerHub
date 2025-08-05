from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at", "is_answered")
    search_fields = ("name", "email", "message")
    list_filter = ("is_answered", "created_at")
    readonly_fields = ("name", "email", "message", "created_at")
    fields = ("name", "email", "message", "created_at", "is_answered", "reply")
