from django import forms
from html_sanitizer import Sanitizer

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100, label='Име')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}), label='Съобщение')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError("Името трябва да е поне 2 символа.")
        return name

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 10:
            raise forms.ValidationError("Съобщението трябва да е поне 10 символа.")
        sanitizer = Sanitizer()
        return sanitizer.sanitize(message)
