from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .models import Event
from .forms import EventForm
from .services import get_user_events, set_event_organization_if_missing, user_can_edit_event


class DashboardView(LoginRequiredMixin, ListView):
    template_name = 'events/dashboard.html'
    context_object_name = 'events'

    def get_queryset(self):
        return get_user_events(self.request.user)


class EventListView(ListView):
    model = Event
    context_object_name = 'events'
    paginate_by = 10
    template_name = 'events/event_list.html'


class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'events/event_detail.html'


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('events:dashboard')
    login_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        event = form.save(commit=False)
        if not set_event_organization_if_missing(event, self.request.user):
            messages.error(self.request, "Потребителят няма организация!")
            return self.form_invalid(form)
        event.save()
        messages.success(self.request, "Събитието беше създадено успешно!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Моля, коригирайте грешките по-долу.")
        return super().form_invalid(form)


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('events:dashboard')

    def test_func(self):
        return user_can_edit_event(self.request.user, self.get_object())

    def form_valid(self, form):
        messages.success(self.request, "Събитието беше обновено успешно!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Моля, коригирайте грешките по-долу.")
        return super().form_invalid(form)


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('events:dashboard')

    def test_func(self):
        return user_can_edit_event(self.request.user, self.get_object())

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Събитието беше изтрито успешно.")
        return super().delete(request, *args, **kwargs)


class HomeView(TemplateView):
    template_name = 'home.html'
