from django.contrib.auth.models import Group
from .models import VolunteerProfile

def create_profile_and_add_staff(user):
    user.is_staff = True
    user.save()
    VolunteerProfile.objects.create(user=user)
    try:
        staff_group = Group.objects.get(name='staff')
        user.groups.add(staff_group)
    except Group.DoesNotExist:
        pass
