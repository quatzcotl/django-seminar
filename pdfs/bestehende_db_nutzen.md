# Bestehende Datenbank nutzen

## Schritt 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'deine_datenbank',
        'USER': 'dein_benutzer',
        'PASSWORD': 'dein_passwort',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

## Schritt 2
App erstellen 

    python manage.py startapp myapp

Eintragen in INSTALLED_APPS

## Schritt 3

    python manage.py inspectdb > myapp/models.py

## Schritt 4

    class Customer(models.Model):
        id = models.IntegerField(primary_key=True)
        name = models.CharField(max_length=255)
        email = models.EmailField()

        class Meta:
            managed = False  # wichtig! sonst versucht Django, die Tabelle zu migrieren
            db_table = 'customer'
