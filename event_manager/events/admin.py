from django.contrib import admin
from .models import Category, Event


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "author", "date", "category", "is_active"]

    # diese Attribute sind anklickbar
    list_display_links = ["id", "name"]
    actions = ["set_active", "set_inactive"]

    # Suchbox, in der in name und subtitle gesucht wird
    search_fields = ["name", "sub_title"]

    def set_active(self, request, queryset):
        """Setze alle Events des Querysets auf aktiv."""
        # queryset => ausgewählten Events
        queryset.update(is_active=True)

    def set_inactive(self, request, queryset):
        """Setze alle Events des Querysets auf inaktiv."""
        queryset.update(is_active=False)
