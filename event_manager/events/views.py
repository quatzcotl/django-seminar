import logging

from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpRequest, Http404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.shortcuts import render, get_object_or_404, redirect

from .models import Category, Event
from .forms import CategoryForm, EventForm

logger = logging.getLogger(__name__)  # erstellt Logger Instanz


class EventUpdateView(SuccessMessageMixin, UpdateView):
    """
    View zum Update eines Events
    http://127.0.0.1:8000/events/3/update
    """

    model = Event
    form_class = EventForm
    success_message = "Das Event wurde erfolgreich aktualisiert"


class EventCreateView(SuccessMessageMixin, CreateView):
    """
    View zum Anlegen eines Events
    http://127.0.0.1:8000/events/create
    """

    model = Event
    form_class = EventForm
    success_message = "Das Event wurde erfolgreich eingetragen"

    def form_valid(self, form):
        """wird immer aufgerufen, wenn das Formular valide ist."""
        form.instance.author = self.request.user
        return super().form_valid(form)


def category_update(request, pk):
    """
    View zum Updaten einer kategorie
    http://127.0.0.1:8000/events/categories/3/update
    """
    instance = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=instance)
    if form.is_valid():
        category = form.save()
        return redirect("events:category-detail", category.pk)

    return render(
        request,
        "events/category_form.html",
        {"form": form},
    )


def category_create(request: HttpRequest):
    """
    View zum Anlegen einer Kategorie
    http://127.0.0.1:8000/events/categories/create
    """
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()  # legt eine neue Kategorie an
            # return redirect("events:categories")  # auf die Übersichtsseite
            return redirect("events:category-detail", category.pk)
    else:
        form = CategoryForm()  # leeres Formular

    return render(
        request,
        "events/category_form.html",
        {"form": form},
    )


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
