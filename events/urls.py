from django.urls import path
from .views import (
    HomeView,
    EventListView,
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    DashboardView,
    EventDeleteView,
)
from rest_framework.routers import DefaultRouter
from .api import EventViewSet

app_name = "events"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("events/", EventListView.as_view(), name="event-list"),
    path("event/<int:pk>/", EventDetailView.as_view(), name="event-detail"),
    path("event/create/", EventCreateView.as_view(), name="event-create"),
    path("event/<int:pk>/edit/", EventUpdateView.as_view(), name="event-update"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("event/<int:pk>/delete/", EventDeleteView.as_view(), name="event-delete"),
]


router = DefaultRouter()
router.register(
    r"events", EventViewSet, basename="event"
)


