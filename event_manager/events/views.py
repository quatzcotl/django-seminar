from django.http import HttpResponse
from django.shortcuts import render
from .models import Category


def hello_world(request):
    """Eine erste Test-View.

    bekommt ein Http-Request-Objekt übergeben
    http://127.0.0.1:8000/events/hello-world
    """
    c = Category.objects.get(pk=1)
    print(c)
    return HttpResponse("Hallo Welt")
