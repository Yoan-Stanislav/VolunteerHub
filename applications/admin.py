from django.contrib import admin
from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("user", "event", "created_at")
    list_filter = ("created_at",)
    date_hierarchy = "created_at"
    search_fields = ("user__username", "event__title")
