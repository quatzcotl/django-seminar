from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from events.models import Event


class Command(BaseCommand):

    def handle(self, *args, **options):

        all_events = Event.objects.all()
        print(all_events)
