from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "category", "organization", "capacity")
    list_filter = ("category", "date", "organization")
    search_fields = ("title", "description")
    ordering = ("-date",)

    def get_inlines(self, request, obj=None):
        # динамично създаваме Inline, когато всичко вече е заредено
        from django.apps import apps
        Application = apps.get_model("applications", "Application")

        class ApplicationInline(admin.TabularInline):
            model = Application
            extra = 0
            fields = ("user", "status", "message", "created_at")
            readonly_fields = ("user", "created_at")
            can_delete = False
            show_change_link = True

        return [ApplicationInline]
