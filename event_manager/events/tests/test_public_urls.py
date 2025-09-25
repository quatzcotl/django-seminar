"""
Öffentlich erreichbare URLs testen, z.b. Event-Übersicht
"""

from datetime import timedelta
from django.utils import timezone
from django.test import Client, TestCase
from django.urls import reverse

from events.models import Event, Category
from user.factories import UserFactory


def create_user():
    return UserFactory()


class EventUrlTest(TestCase):
    def setUp(self):
        """Wird für jeden Test ausgeführt"""
        self.category = Category.objects.create(name="Test Category")
        self.event = Event.objects.create(
            name="Test Event 123",
            author=create_user(),
            category=self.category,
            date=timezone.now() + timedelta(days=1),
        )
        self.client = Client()  # Browser für Arme

    def test_event_overview(self):
        """Prüfen, ob die Event-Übersicht öffentlich erreichbar ist."""
        url = reverse("events:events")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "events/event_list.html")
        self.assertContains(response, text="Test Event 123")

    def test_event_detail(self):
        """Prüfen, ob die Event-Detailseite öffentlich erreichbar ist."""
        url = reverse("events:event-detail", kwargs={"pk": self.event.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "events/event_detail.html")
        self.assertContains(response, text="Test Event 123")
