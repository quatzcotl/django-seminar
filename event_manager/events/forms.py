"""
Hier werden die Formulare definiert.

Ein forms.ModelForm baut ein Formular auf Basis
des Models auf.
"""

from django import forms
from django.core.exceptions import ValidationError
from .models import Category, Event


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"  # Alle Felder
        # fields = ("name", "sub_title") konkrete Felder auswählen


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"  # Alle Felder
        exclude = ("author",)

        widgets = {
            "date": forms.DateInput(
                format=("%Y-%m-%d %H:%M"), attrs={"type": "datetime-local"}
            ),
        }

    def clean_description(self) -> str:
        """Wird aufgerufen, wenn die Description gespeichert wird."""
        description = self.cleaned_data["description"]

        # Prüft, ob das Wort "verboten" in der Beschreibung vokommt
        if isinstance(description, str) and "verboten" in description:
            raise ValidationError("Verboten darf nicht in der Beschreibung vorkommen!")

        return description
