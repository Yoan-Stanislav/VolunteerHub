from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Application
from .forms import ApplicationForm

class ApplicationListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'applications/application_list.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.filter(user=self.request.user)

class ApplicationCreateView(LoginRequiredMixin, CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'applications/application_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.event_id = self.kwargs['event_pk']
        messages.success(self.request, "Your application has been submitted!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error: Please correct the message and try again.")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('applications:application-list')
