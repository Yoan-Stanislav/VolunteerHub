from django import forms
from .models import Organization
from html_sanitizer import Sanitizer

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'description', 'logo', 'website']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Organization name must be at least 3 characters.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        sanitizer = Sanitizer()
        return sanitizer.sanitize(description)
