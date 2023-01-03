from django.apps import AppConfig


class WorkersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'workers'
    validation_rules = {
        "create": {"name": {"required": True, "type": str}},
        "update":
        {"name": {"required": True, "type": str},
         "worker_id": {"required": True, "type": int}},
        "details": {"worker_id": {"required": True, "type": int}},
        "delete": {"worker_id": {"required": True, "type": int}}}
