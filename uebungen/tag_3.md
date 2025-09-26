
# Tag 3 Übung 

- Formulare, Templates, Verlinkungen
- optional: Messages

#### Crispy Forms
- pip install django-crispy-forms
- pip install crispy-bootstrap5

in den settings.py

INSTALLED_APPS = [
    ..
    "crispy_forms",
    "crispy_bootstrap5",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

#### in category_form.html

{% load crispy_forms_tags %}

<form method="POST">
    {% csrf_token %}
    {{form|crispy}}
...
