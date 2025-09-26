from django.views.generic import TemplateView

from events.models import Event


class HomepageView(TemplateView):
    """Template View zeigt nur Template an."""

    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        # Alles aus dem Kontext steht im Template zur Verfügung
        context["events"] = Event.objects.all()[:3]
        context["data"] = [1, 2, 3, 4]

        return context
