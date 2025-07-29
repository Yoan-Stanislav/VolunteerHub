from django.urls import path
from .views import ApplicationListView, ApplicationCreateView
app_name = 'applications'
urlpatterns = [
    path('', ApplicationListView.as_view(), name='application-list'),
    path('apply/<int:event_pk>/', ApplicationCreateView.as_view(), name='application-create'),
]