from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from events.models import Event
from .serializers import EventSerializer


class EventListCreateAPIView(generics.ListCreateAPIView):
    """
    eine View, um alle User aufzulisten bzw. einen neuen User zu erstellen
    """

    queryset = Event.objects.all()  # Pflichtangabe
    serializer_class = EventSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # perform_create wird immer aufgerufen, wenn ein Objekt erstellt wird
        author = self.request.user
        serializer.save(author=author)
