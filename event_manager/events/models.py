from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    """Das Kategorie Model"""

    class Meta:
        # immer wenn der Model-Name als Repräsentation genutzt wird,
        # wird jetzt verbose genommen.
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorien"

    name = models.CharField(max_length=20, unique=True)  # mandatory
    # null => darf in DB null sein, blank => darf im Formular leer sein
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(
        help_text="Die Beschreibung einer Kategorie", null=True, blank=True
    )

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    """Das Modell eines Events, mit Foreign Key auf Category."""

    class Group(models.IntegerChoices):
        BIG = 10, "große Gruppe"
        SMALL = 2, "kleine Gruppe"
        UNLIMITED = 0, "unbegrenzt"

    name = models.CharField(max_length=20, unique=True)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField()
    min_group = models.PositiveIntegerField(
        choices=Group.choices, default=Group.UNLIMITED
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="events",  # bob.events.all()
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,  # alternativ PROTECT, SET_NULL, SET_DEFAULT
        related_name="events",  # sport.events.all()
    )

    def __str__(self) -> str:
        return self.name
