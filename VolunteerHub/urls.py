from django.contrib import admin
from django.urls import path, include
from events.views import EventListView
from events.api import EventViewSet
from rest_framework.routers import DefaultRouter

# DRF router конфигурация
router = DefaultRouter()
router.register(r"events", EventViewSet, basename="event")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include(("accounts.urls", "accounts"), namespace="accounts")),
    path("", EventListView.as_view(), name="home"),
    path("events/", include(("events.urls", "events"), namespace="events")),
    path(
        "applications/",
        include(("applications.urls", "applications"), namespace="applications"),
    ),
    path(
        "organizations/",
        include(("organizations.urls", "organizations"), namespace="organizations"),
    ),
    path("locations/", include(("locations.urls", "locations"), namespace="locations")),
    path("contact/", include(("core.urls", "contact"), namespace="contact")),
    path("api/", include(router.urls)),  # <-- ТОВА ДОБАВЯ api/events/
]
