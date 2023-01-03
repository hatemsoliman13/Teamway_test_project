from .models import Shift
from workers.models import Worker
from datetime import date


class ShiftService():

    def create(self, date: date,worker: Worker, duration: str):
        shift = Shift(worker=worker,date=date,duration=duration)
        shift.save()
        return shift

    def update(self, worker: Worker, shift_id: int, date: date, duration: str):
        shift = self.get(shift_id)
        shift.worker = worker
        shift.date = date
        shift.duration = duration
        shift.save()
        return shift

    def get(self, shift_id: int):
        return Shift.objects.get(pk=shift_id)

    def delete(self, shift_id: int):
        shift = self.get(shift_id)
        shift.delete()
        return shift
