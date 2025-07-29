from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView
from .models import VolunteerProfile
from .forms import ProfileForm, RegistrationForm
from .services import create_profile_and_add_staff

class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save()
        create_profile_and_add_staff(user)
        messages.success(self.request, "Registration successful! You can now log in.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = VolunteerProfile
    template_name = 'accounts/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self):
        profile, _ = VolunteerProfile.objects.get_or_create(user=self.request.user)
        return profile

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = VolunteerProfile
    form_class = ProfileForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('accounts:profile')  # ПРЕДПОЛАГАМ правилния namespace!

    def get_object(self):
        profile, _ = VolunteerProfile.objects.get_or_create(user=self.request.user)
        return profile

    def form_valid(self, form):
        messages.success(self.request, "Profile updated successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)
