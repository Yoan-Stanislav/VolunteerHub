from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView
from .models import VolunteerProfile, Message
from .forms import ProfileForm, RegistrationForm
from django import forms
from django.contrib.auth.models import User


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:login")

    def form_valid(self, form):
        messages.success(self.request, "Registration successful! You can now log in.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = VolunteerProfile
    template_name = "accounts/profile_detail.html"
    context_object_name = "profile"

    def get_object(self):
        profile, _ = VolunteerProfile.objects.get_or_create(user=self.request.user)
        return profile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = VolunteerProfile
    form_class = ProfileForm
    template_name = "accounts/profile_edit.html"
    success_url = reverse_lazy("accounts:profile")  # ПРЕДПОЛАГАМ правилния namespace!

    def get_object(self):
        profile, _ = VolunteerProfile.objects.get_or_create(user=self.request.user)
        return profile

    def form_valid(self, form):
        messages.success(self.request, "Profile updated successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'body']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        # Показва само другите потребители като опция за получател
        self.fields['recipient'].queryset = User.objects.exclude(id=user.id)

# INBOX
@login_required
def inbox(request):
    messages_in = Message.objects.filter(recipient=request.user).order_by('-date_sent')
    return render(request, "accounts/inbox.html", {"messages": messages_in})

# OUTBOX
@login_required
def outbox(request):
    messages_out = Message.objects.filter(sender=request.user).order_by('-date_sent')
    return render(request, "accounts/outbox.html", {"messages": messages_out})

# SEND MESSAGE
@login_required
def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST, user=request.user)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            messages.success(request, "Съобщението беше изпратено!")
            return redirect("accounts:outbox")
        else:
            messages.error(request, "Грешка при изпращане на съобщението.")
    else:
        form = MessageForm(user=request.user)
    return render(request, "accounts/send_message.html", {"form": form})