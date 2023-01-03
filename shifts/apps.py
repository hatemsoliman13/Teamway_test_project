from django.apps import AppConfig
from datetime import date
from .enums import ShiftDuration


class ShiftsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shifts'
    validation_rules = {
        "create":
        {"worker_id": {"required": True, "type": int},
         "date": {"required": True, "type": date},
         "duration":
         {"required": True, "type": str,
          "values": list(ShiftDuration)}},
        "update":
        {"shift_id": {"required": True, "type": int},
         "worker_id": {"required": True, "type": int},
         "date": {"required": True, "type": date},
         "duration":
         {"required": True, "type": str,
          "values": list(ShiftDuration)}},
        "details": {"shift_id": {"required": True, "type": int}},
        "delete": {"shift_id": {"required": True, "type": int}}}
