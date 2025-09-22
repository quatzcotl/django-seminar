""" 
EVENTS URLs: alle URLs die für die Event-app sind
"""
from django.urls import path 
from . import views


urlpatterns = [
    # http://127.0.0.1:8000/events/hello-world
    path("hello-world", views.hello_world, name="hello-world"),
]
