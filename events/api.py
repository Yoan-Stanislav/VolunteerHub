from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        user = self.request.user
        org = user.organizations.first()
        if not org:
            from rest_framework.exceptions import ValidationError
            raise ValidationError({"organization": "Потребителят няма организация!"})
        serializer.save(organization=org)

