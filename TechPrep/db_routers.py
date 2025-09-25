# db_routers.py

class BasicsRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'basics':
            return 'basics'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'basics':
            return 'basics'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'basics':
            return db == 'basics'
        return None
    
class SignalsRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'signals':
            return 'signals'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'signals':
            return 'signals'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'signals':
            return db == 'signals'
        return None