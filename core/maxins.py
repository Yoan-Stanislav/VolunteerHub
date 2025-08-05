from django.contrib.auth.mixins import UserPassesTestMixin


class OwnerOrSuperuserRequiredMixin(UserPassesTestMixin):
    "Достъп само за собственика на обекта или суперпотребител."

    def test_func(self):
        obj = self.get_object()
        user = getattr(obj, "user", None)
        if user is None and hasattr(obj, "organization"):
            user = getattr(obj.organization, "user", None)
        return self.request.user.is_superuser or user == self.request.user
