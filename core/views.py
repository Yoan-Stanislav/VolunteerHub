from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import ContactUsForm


class ContactView(FormView):
    template_name = "core/contact.html"
    form_class = ContactUsForm
    success_url = reverse_lazy("contact:contact")

    def form_valid(self, form):
        # Тук изпращаме email или записваме в базата:
        # name = form.cleaned_data['name']
        # email = form.cleaned_data['email']
        # message = form.cleaned_data['message']
        messages.success(
            self.request, "Благодарим за Вашето съобщение! Ще се свържем с Вас."
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Моля, коригирайте грешките по-долу.")
        return super().form_invalid(form)
