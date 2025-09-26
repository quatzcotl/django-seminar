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
- Django (Baptiste Darthenay) batisteo.vscode-django
- Python Extension Microsoft
- Black Formatter Microsoft
- Rest Client API von donedb (donebd.rest-client-api)

# Drittanbieter - Tools für Django
- Django DebugToolbar: https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

## VS Code Settings Json

    {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true,
        "files.autoSave": "onFocusChange",
        "explorer.compactFolders": false,
        "workbench.tree.indent": 26
    }

# Tools zur Dokumentation
- https://www.mkdocs.org/
- https://lyz-code.github.io/blue-book/

# UML rendern
- Django Extensions installieren (pip install django-extensions)
- python manage.py graph_models -a > graphout
- graphout öffnen und kopieren nach:
- https://dreampuf.github.io/GraphvizOnline/?engine=dot