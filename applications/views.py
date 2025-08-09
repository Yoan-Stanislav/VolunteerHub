from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView

from events.models import Event
from .models import Application
from .forms import ApplicationForm


class ApplicationListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = "applications/application_list.html"
    context_object_name = "applications"

    def get_queryset(self):
        return (
            Application.objects
            .filter(user=self.request.user)
            .select_related("event")
        )


class ApplicationCreateView(LoginRequiredMixin, CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = "applications/application_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.event = get_object_or_404(Event, pk=self.kwargs["event_pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # вече присъединен?
        if Application.objects.filter(user=self.request.user, event=self.event).exists():
            messages.info(self.request, "Вече сте присъединени към това събитие.")
            return redirect("events:event-detail", pk=self.event.pk)

        # капацитет?
        if Application.objects.filter(event=self.event).count() >= self.event.capacity:
            messages.error(self.request, "Няма свободни места за това събитие.")
            return redirect("events:event-detail", pk=self.event.pk)

        app = form.save(commit=False)
        app.user = self.request.user
        app.event = self.event
        app.status = "APP"     # директно одобрен (присъединен)
        app.save()

        messages.success(self.request, "Присъединихте се успешно!")
        return redirect("events:event-detail", pk=self.event.pk)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["event"] = self.event
        return ctx
