# Django Seminar

https://github.com/quatzcotl/django-seminar

## INSTALLATION

### Environment erstellen und aktivieren
```
    python -m venv .venv
    .venv\Scripts\activate
```

### Django installieren
pip install django

### Runserver starten
python manage.py runserver

### Admin Oberfläche
127.0.0.1:8000/admin

# Django Debugtoolbar installieren
- pip install django-debug-toolbar
- Django Debug Toolbar in den Settings registrieren:

```
if DEBUG:
    INSTALLED_APPS.extend(["debug_toolbar"])
    MIDDLEWARE.extend(["debug_toolbar.middleware.DebugToolbarMiddleware"])
    INTERNAL_IPS = ("127.0.0.1",)
```

- Django Debug Toolbar Verlinken (Projekt urls.py):

```
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    ...
] + debug_toolbar_urls()
```

# Drittanbieter Extensions für Django VS Code
- batisteo.vscode-django
- Python Extension Microsoft
- Black Formatter Microsoft

# Drittanbieter - Tools für Django
- Django DebugToolbar: https://django-debug-toolbar.readthedocs.io/en/latest/installation.html