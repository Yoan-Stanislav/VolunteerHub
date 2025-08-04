from django.apps import AppConfig
from django.db.models.signals import post_migrate


def create_user_groups(sender, **kwargs):
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType

    # 1) super-admins
    super_admins, created = Group.objects.get_or_create(name="super-admins")
    if created:
        all_perms = Permission.objects.all()
        super_admins.permissions.set(all_perms)

    # 2) staff
    staff, created = Group.objects.get_or_create(name="staff")
    if created:
        # Първо проверяваме дали ContentType ги има!
        ct_event = ContentType.objects.filter(app_label="events", model="event").first()
        ct_location = ContentType.objects.filter(
            app_label="locations", model="location"
        ).first()

        if ct_event and ct_location:
            perms = Permission.objects.filter(
                content_type__in=[ct_event, ct_location],
                codename__in=[
                    "view_event",
                    "change_event",
                    "view_location",
                    "change_location",
                ],
            )
            staff.permissions.set(perms)
        # Ако липсват – просто прескачаме. При следващ run/миграция ще ги сетне!


from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = "accounts"

    def ready(self):
        import accounts.signals
