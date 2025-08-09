from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at", "is_answered")
    search_fields = ("name", "email", "message", "reply")
    list_filter = ("is_answered", "created_at")
    readonly_fields = ("name", "email", "message", "created_at")
    fields = ("name", "email", "message", "created_at", "reply", "is_answered")

    def save_model(self, request, obj, form, change):
        reply = form.cleaned_data.get("reply")

        obj.is_answered = bool(reply)
        super().save_model(request, obj, form, change)

    @admin.action(description="Маркирай като отговорено")
    def mark_answered(self, request, queryset):
        queryset.update(is_answered=True)

    @admin.action(description="Маркирай като НЕотговорено")
    def mark_unanswered(self, request, queryset):
        queryset.update(is_answered=False)

    actions = ("mark_answered", "mark_unanswered")
