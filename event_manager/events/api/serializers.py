"""
Serializers entsprechen in etwa dem Formular aus Django
"""

from rest_framework import serializers
from events.models import Event, Category


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("name", "category", "date", "min_group")
