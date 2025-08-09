from django.contrib import admin, messages
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("user", "event", "status", "created_at")
    list_filter = ("status", "created_at", "event")
    search_fields = ("user__username", "user__email", "event__title", "message")
    autocomplete_fields = ("user", "event")
    readonly_fields = ("created_at",)
    actions = ["approve", "reject"]

    @admin.action(description="Одобри избраните")
    def approve(self, request, queryset):
        updated = queryset.update(status="APP")
        self.message_user(request, f"Одобрени: {updated}", level=messages.SUCCESS)

    @admin.action(description="Отхвърли избраните")
    def reject(self, request, queryset):
        updated = queryset.update(status="REJ")
        self.message_user(request, f"Отхвърлени: {updated}", level=messages.Warning)
