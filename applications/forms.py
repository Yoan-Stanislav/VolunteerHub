import bleach
from django import forms
from .models import Application
from html_sanitizer import Sanitizer


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["message"]
        widgets = {"message": forms.Textarea(attrs={"rows": 4})}

    def clean_message(self):
        message = self.cleaned_data.get("message")
        if not message or len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long.")
        sanitizer = Sanitizer()
        return sanitizer.sanitize(message)
