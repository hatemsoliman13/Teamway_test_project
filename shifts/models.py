from django.db import models
from workers.models import Worker

# Create your models here.


class Shift(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def as_dict(self):
        return {"id": self.id, "worker": [self.worker.as_dict()], "date": self.date, "duration": self.duration}

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["worker", "date"],
                name="worker_shift_per_day_constraint")]
