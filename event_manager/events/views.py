import logging

from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Category, Event

logger = logging.getLogger(__name__)  # erstellt Logger Instanz


class EventDetailView(DetailView):
    """
    Template-Name: event_detail.html
    Context: object (alternativ: event)
    """

    model = Event


class EventListView(ListView):
    """Alle Events auflisten.
    http://127.0.0.1:8000/events

    Template Schama:
    - liegt unter events/templates/events
    - heisst modelname_list.html
    - z.b. events/templates/events/event_list.html

    im Template kann man auf die liste via object_list
    zugreifen
    """

    model = Event


def category_detail(request, pk: int):
    """
    Anzeigen der Kategorie-Detailseite
    http://127.0.0.1:8000/events/categories/3
    """
    category = get_object_or_404(Category, pk=pk)  # ist shortcut für ff
    # try:
    #     category = Category.objects.get(pk=pk)
    # except Category.DoesNotExist:
    #     logger.error("Die ID %s gibt es nicht mehr", pk)
    #     raise Http404("Diese Seite existiert nicht mehr!")

    return render(
        request,
        "events/category_detail.html",
        {
            "category": category,
        },
    )


def categories(request):
    """
    Auflisten von Kategorien
    http://127.0.0.1:8000/events/categories
    """
    categories = Category.objects.all()
    return render(
        request,
        "events/categories.html",
        {
            "categories": categories,
        },
    )


def hello_world(request):
    """Eine erste Test-View.

    bekommt ein Http-Request-Objekt übergeben
    http://127.0.0.1:8000/events/hello-world
    """
    c = Category.objects.all()
    return HttpResponse(",".join([el.name for el in c]))
