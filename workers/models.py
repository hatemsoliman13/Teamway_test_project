from django.db import models

# Create your models here.


class Worker(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def as_dict(self):
        return {"id": self.id, "name": self.name}
