
# Django Tutorial: Datenbank-Constraints

Datenbank-Constraints (Einschränkungen) sind Regeln, die von der Datenbank erzwungen werden, um Datenintegrität und Konsistenz sicherzustellen.
Django bietet eine elegante Möglichkeit, solche Constraints direkt im `models.py` zu definieren. Beim Migrieren (`makemigrations` + `migrate`) erzeugt Django die entsprechenden SQL-Constraints in der Datenbank.

## Motivation

* **Integrität**: Sicherstellen, dass keine ungültigen oder widersprüchlichen Daten gespeichert werden.
* **Performance**: Viele Validierungen können direkt durch die Datenbank effizienter erzwungen werden.
* **Single Source of Truth**: Regeln sind nicht nur in der Applikationslogik (Python), sondern auch in der Datenbank verankert.

Beispiel: Es reicht nicht, nur im Django-Formular zu prüfen, ob ein Feld > 0 ist. Wenn Daten durch API oder Import eingefügt werden, muss auch die Datenbank die Regel erzwingen.

---

## 1. `UniqueConstraint` (Eindeutigkeit erzwingen)

```python
from django.db import models

class Booking(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "event"],
                name="unique_user_event_booking"
            )
        ]
```

### Erklärung

* Ein User darf ein Event nur einmal buchen.
* Django erzeugt einen `UNIQUE INDEX` auf (`user_id`, `event_id`).

### Umgang in einer View/DRF-API

```python
from django.db import IntegrityError
from django.http import JsonResponse


def book_event(request, event_id):
    booking = Booking(user=request.user, event_id=event_id)
    try:
        booking.full_clean()  # führt Feld- und Model-Validierung aus
        booking.save()
        return JsonResponse({"message": "Buchung erfolgreich"}, status=201)
    except ValidationError as e:
        return JsonResponse({"error": e.message_dict}, status=400)
    except IntegrityError:
        return JsonResponse({"error": "User hat dieses Event bereits gebucht"}, status=400)

```

* **HTTP 201**: Erfolg.
* **HTTP 400**: Ungültige Anfrage (Constraint verletzt).

### Umgang in einer Django-Generic Create View

```python
class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "bookings/booking_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.event_id = self.kwargs["event_id"]
        try:
            return super().form_valid(form)
        except IntegrityError:
            return HttpResponseBadRequest("User hat dieses Event bereits gebucht")
```

## 2. `CheckConstraint` (Bedingungen auf Werte)

```python
from django.db import models
from django.db.models import Q

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(price__gte=0),
                name="price_non_negative"
            ),
            models.CheckConstraint(
                check=Q(discount__gte=0) & Q(discount__lte=100),
                name="discount_between_0_and_100"
            ),
        ]
```

### Erklärung

* Preis darf nicht negativ sein.
* Rabatt muss zwischen 0 und 100 liegen.

### Umgang in einer View/DRF-API

```python
from django.views.decorators.http import require_POST
from django.db import IntegrityError
from django.http import JsonResponse

@require_POST
def create_product(request):
    try:
        product = Product.objects.create(
            name=request.POST["name"],
            price=request.POST["price"],
            discount=request.POST.get("discount", 0),
        )
        return JsonResponse({"id": product.id, "message": "Produkt angelegt"}, status=201)
    except IntegrityError:
        return JsonResponse({"error": "Ungültiger Preis oder Rabatt"}, status=400)
```

* **HTTP 201**: Neues Produkt erfolgreich.
* **HTTP 400**: Preis oder Rabatt verletzt Constraint.


### Umgang in einer View/DRF-API

```python
from django.views.generic import CreateView
from django.http import HttpResponseBadRequest
from django.db import IntegrityError
from django.shortcuts import redirect
from .models import Product

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/product_form.html"

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError:
            return HttpResponseBadRequest("Ungültiger Preis oder Rabatt")
```

## 3. `ExclusionConstraint` (nur in PostgreSQL)

```python
from django.db import models
from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.fields import DateTimeRangeField
from django.contrib.postgres.fields import RangeOperators
from django.db.models import F

class RoomBooking(models.Model):
    room = models.IntegerField()
    timeslot = DateTimeRangeField()

    class Meta:
        constraints = [
            ExclusionConstraint(
                name="exclude_overlapping_bookings",
                expressions=[
                    (F("room"), RangeOperators.EQUAL),
                    (F("timeslot"), RangeOperators.OVERLAPS),
                ],
            )
        ]
```

### Erklärung

* Zwei Buchungen für denselben Raum dürfen sich zeitlich nicht überschneiden.
* Nur PostgreSQL unterstützt diese Art von Constraint.

### Umgang in einer View/DRF-API

```python
from django.db import IntegrityError
from django.http import JsonResponse

def book_room(request):
    try:
        booking = RoomBooking.objects.create(
            room=request.POST["room"],
            timeslot=request.POST["timeslot"],  # z. B. ['2025-09-21 10:00', '2025-09-21 12:00']
        )
        return JsonResponse({"message": "Raum gebucht"}, status=201)
    except IntegrityError:
        return JsonResponse({"error": "Zeitraum überschneidet sich mit bestehender Buchung"}, status=409)
```

* **HTTP 201**: Erfolg.
* **HTTP 409 (Conflict)**: Überschneidung erkannt.

---

## Technischer Hintergrund

* **SQL-Ebene**: Django generiert `ALTER TABLE ... ADD CONSTRAINT ...` Statements.
* **Migrationen**: Constraints leben in den Migrationsdateien. Änderungen (z. B. neuer Name, neue Bedingung) erzeugen neue Migrationen.
* **Validierung**: Django-Forms prüfen meist schon vorher, aber die **Datenbank** ist die letzte Instanz, die garantiert, dass Regeln niemals verletzt werden – auch bei parallelen Schreibzugriffen.

---

## Fazit

* Verwende Constraints, um Datenintegrität **dauerhaft** sicherzustellen.
* Typische Anwendungsfälle: Eindeutigkeit (`UniqueConstraint`), Bereichsprüfungen (`CheckConstraint`), Überschneidungsvermeidung (`ExclusionConstraint`).
* Passende HTTP-Responses geben dem Client direktes Feedback:

  * 201 = erstellt
  * 400 = ungültige Eingabe
  * 409 = Konflikt


