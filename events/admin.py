from django.contrib import admin
from events.models import Event
from applications.models import Application


class ApplicationInline(admin.TabularInline):
    model = Application
    extra = 0
    fields = ("user", "message", "created_at")
    readonly_fields = ("created_at",)


@admin.action(description="Approve selected applications")
def approve_applications(modeladmin, request, queryset):
    updated = queryset.update(message="APPROVED")
    modeladmin.message_user(request, f"{updated} application(s) approved.")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "category", "organization", "capacity")
    list_filter = ("category", "date")
    search_fields = ("title", "description")
    ordering = ("-date",)
    inlines = (ApplicationInline,)
    actions = (approve_applications,)
