from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    # http://127.0.0.1:8000
    path("", views.HomepageView.as_view(), name="homepage"),
]
