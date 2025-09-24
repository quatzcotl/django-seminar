
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


CREATE TABLE "events_event" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(20) NOT NULL UNIQUE, "sub_title" varchar(200) NULL, "description" text NULL, 
"is_active" bool NOT NULL, 
"category_id" bigint NOT NULL REFERENCES "events_category" ("id") DEFERRABLE INITIALLY DEFERRED, 
"date" datetime NOT NULL, 
"author_id" bigint NOT NULL REFERENCES "user_user" ("id") DEFERRABLE INITIALLY DEFERRED, 
"min_group" integer unsigned NOT NULL CHECK ("min_group" >= 0), CONSTRAINT "min_group_less_10" CHECK ("min_group" <= 10))
