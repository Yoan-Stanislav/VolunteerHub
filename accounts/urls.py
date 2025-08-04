from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView, ProfileDetailView, ProfileUpdateView

app_name = "accounts"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="events:event-list"),
        name="logout",
    ),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileDetailView.as_view(), name="profile"),
    path("profile/edit/", ProfileUpdateView.as_view(), name="profile-edit"),
]
