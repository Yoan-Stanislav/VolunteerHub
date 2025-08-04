# events/services.py
from .models import Event


def get_user_organizations(user):
    return user.organizations.all()


def get_user_events(user):
    return Event.objects.filter(organization__in=get_user_organizations(user))


def set_event_organization_if_missing(event, user):
    if not event.organization:
        org = user.organizations.first()
        if org:
            event.organization = org
            return True
        else:
            return False
    return True


def user_can_edit_event(user, event):
    return user == event.organization.user or user.is_superuser
