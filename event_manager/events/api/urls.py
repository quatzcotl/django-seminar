from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import EventListCreateAPIView

urlpatterns = [
    # GET api/events => zeigt Liste von Events
    # POST api/events => legt neuen Event an
    path("events", EventListCreateAPIView.as_view(), name="event-api-list"),
    # POST api/token => erhalte ich den Token für den User
    path("token", obtain_auth_token, name="user-token"),
]
