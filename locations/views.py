from django.views.generic import ListView, DetailView
from .models import Location


class LocationListView(ListView):
    model = Location
    template_name = "locations/location_list.html"
    context_object_name = "locations"


class LocationDetailView(DetailView):
    model = Location
    template_name = "locations/location_detail.html"
    context_object_name = "location"
