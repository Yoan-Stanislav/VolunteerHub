from django.contrib import admin
from accounts.models import VolunteerProfile


@admin.register(VolunteerProfile)
class VolunteerProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "birth_date")
    search_fields = ("user__username", "user__first_name", "user__last_name")
