from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import VolunteerProfile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, help_text="Required. Enter a valid email address."
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if len(username) < 3:
            raise forms.ValidationError("Username must be at least 3 characters.")
        return username


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if first_name and len(first_name) < 2:
            raise forms.ValidationError("First name must be at least 2 characters.")
        return first_name


class ProfileForm(forms.ModelForm):
    class Meta:
        model = VolunteerProfile
        fields = ["phone", "birth_date", "skills"]
        widgets = {
            "birth_date": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if phone and not phone.isdigit():
            raise forms.ValidationError("Phone must contain only digits.")
        return phone

    def clean_skills(self):
        skills = self.cleaned_data.get("skills")
        if skills and len(skills) < 3:
            raise forms.ValidationError("Please list at least one skill (3+ chars).")
        return skills
