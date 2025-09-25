"""
Formulare der Event-App testen
"""

from datetime import timedelta
from django.utils import timezone
from django.test import Client, TestCase
from django.urls import reverse

from events.models import Event, Category
from user.factories import UserFactory


def create_user():
    return UserFactory()


def show_form_errors(response):
    if response.context and "form" in response.context:
        print(response.context["form"].errors)


class EventFormTest(TestCase):
    def setUp(self):
        """Wird für jeden Test ausgeführt"""
        self.category = Category.objects.create(name="Test Category")
        self.event = Event.objects.create(
            name="Test Event 123",
            author=create_user(),
            category=self.category,
            date=timezone.now() + timedelta(days=1),
        )
        self.user = create_user()
        self.client = Client()  # Browser für Arme

    def test_create_event(self):
        """Testen, ob ein Event per Formular angelegt werden kann."""
        # User einloggen
        self.client.force_login(self.user)
        url = reverse("events:event-create")
        # GET request testen
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "events/event_form.html")

        # POST request testen
        payload = {
            "name": "Test Event 42",
            "category": self.category.pk,
            "date": (timezone.now() + timedelta(days=1)),
            "min_group": 0,
        }

        response = self.client.post(url, payload)
        # show_form_errors(response)# Falls es fehlschlägt, kann man sich Fehler ausgeben lassen
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Event.objects.filter(name=payload["name"]).exists())

    def test_invalid_date(self):
        """Testen, ob ein Event in der Vergangenheit nicht eingetragen wird."""
        self.client.force_login(self.user)
        url = reverse("events:event-create")

        payload = {
            "name": "Test Event 42",
            "category": self.category.pk,
            "date": (timezone.now() + timedelta(days=-1)),
            # "min_group": 0,
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Event.objects.filter(name=payload["name"]).exists())
