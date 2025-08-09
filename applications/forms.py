from django import forms
from html_sanitizer import Sanitizer
from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["message"]
        widgets = {"message": forms.Textarea(attrs={"rows": 4})}

    def clean_message(self):
        message = self.cleaned_data.get("message", "")
        if message and len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long.")
        return Sanitizer().sanitize(message)

