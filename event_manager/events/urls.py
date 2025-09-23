"""
event_manager/events/urls.py
EVENTS URLs: alle URLs die für die Event-app sind
"""

from django.urls import path
from . import views

app_name = "events"  # eine URL im Template besteht aus app_name:path-name

urlpatterns = [
    # http://127.0.0.1:8000/events
    path("", views.EventListView.as_view(), name="events"),
    # http://127.0.0.1:8000/events/3
    path("<int:pk>", views.EventDetailView.as_view(), name="event-detail"),
    # http://127.0.0.1:8000/events/hello-world
    path("hello-world", views.hello_world, name="hello-world"),
    # http://127.0.0.1:8000/events/categories
    path("categories", views.categories, name="categories"),
    # http://127.0.0.1:8000/events/categories/3
    path("categories/<int:pk>", views.category_detail, name="category-detail"),
]
