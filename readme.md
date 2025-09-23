# Django Seminar

https://github.com/quatzcotl/django-seminar

## Tag 1 
- Einführung
- Models, Querysets, Adminoberfläche

## Tag 1 Übung
ERstelle ein eigenes Django-Projekt
Erstelle dazu ein neues virtuelles Environment, installiere Django
App erstellen, Models erstellen, Migrationen, Adminoberfläche
Thema Eurer Wahl, zb. Company-Employees (1:N)

1. Projekt anlegen (startproject)
2. App anlegen (startapp company)
2b. Migration
3. App registrieren (in den settings INSTALLED_APPS)
4. Model anlegen (zb. Company, Employee)
5. Makemigrations
6. Migrate
7. in der admin.py das Model registrieren
8. einen Superuser anlegen (createsuperuser)
9. Login in Adminoberfläche


1. Projekt anlegen
----------------------------
- mkdir company_project
- cd company_project
- django-admin startproject company_manager

2. App anlegen
----------------------------
- cd company_manager
- python manage.py startapp company 

3. Die Migrationsdateien von Django migrieren
-------------------------------------------------
- python manage.py migrate

4. Models anlegen
-------------------
- company/models.py öffnen
- Models definieren

5. company App in den settings registrieren
-------------------------------------------------
INSTALLED_APPS[
    ....
    "company",
]

6. Company App migrieren
-------------------------------------------------
python manage.py makemigrations company
python manage.py migrate company

7. in der admin.py das Model registrieren
-------------------------------------------------
company/admin.py öffnen
Models als Admin registrieren

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass

8. Superuser anlegen
-------------------------------------------------
python manage.py createsuperuser


9. Login in Adminoberfläche
-------------------------------------------------
http:/127.0.0.1:8000/admin

10. Eine View (siehe event_manager/events/views.py)
-------------------------------------------------
eine View anlegen die eine kommaseparierter


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

### Admin 
127.0.0.1:8000/admin

# Tag 2 Übung

- List / DetailViews für die Übungs-Applikation
- Verlinkung (urls.py)
- Templates für List und Detail


# Drittanbieter Extensions für Django VS Code
- batisteo.vscode-django