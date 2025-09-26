class LegacyRouter:
    """
    Router für SCREW_DATA: Modelle aus der App 'desoutter' lesen nur von SCREW_DATA.
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label == "desoutter":
            return "SCREW_DATA"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == "desoutter":
            return None  # Schreibzugriff unterbinden
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == "desoutter" and obj2._meta.app_label == "desoutter":
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == "desoutter":
            return False  # Keine Migration für legacy-Modelle
        return None


DATABASE_ROUTERS = ["desoutter.db_router.LegacyRouter"]
