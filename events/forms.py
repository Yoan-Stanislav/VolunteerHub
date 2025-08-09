from django import forms
from .models import Event
from html_sanitizer import Sanitizer

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "title",
            "description",
            "date",
            "capacity",
            "category",
            "organization",
            "location",
        ]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        # подаваме текущия потребител към формата
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        # показваме само организациите на този потребител
        if self.user and hasattr(self.user, "organizations"):
            self.fields["organization"].queryset = self.user.organizations.all()

        # при редакция – не позволяваме смяна на организацията
        if self.instance and self.instance.pk:
            self.fields["organization"].disabled = True

    def clean_capacity(self):
        capacity = self.cleaned_data.get("capacity")
        if capacity is not None and capacity < 1:
            raise forms.ValidationError("Capacity must be at least 1.")
        return capacity

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters.")
        return title

    def clean_description(self):
        description = self.cleaned_data.get("description")
        sanitizer = Sanitizer()
        return sanitizer.sanitize(description)
