from django.test import TestCase
from workers.services import WorkerService
from workers.models import Worker
from .services import ShiftService
from .models import Shift
from .enums import ShiftDuration
import datetime

# Create your tests here.


def create_worker(name: str) -> Worker:
    worker_service = WorkerService()
    return worker_service.create(name)


def create_shift(worker: Worker, date: datetime.date,
                 duration: ShiftDuration) -> Shift:
    shift_service = ShiftService()
    return shift_service.create(
        datetime.datetime.now().date(),
        worker, duration)


class ShiftServiceTests(TestCase):
    def test_create(self):
        worker = create_worker("John Doe")
        created_shift = create_shift(
            worker, datetime.datetime.now().date(),
            ShiftDuration.FIRST_SHIFT)
        found_shift = Shift.objects.get(pk=1)
        self.assertEqual(created_shift, found_shift)

    def test_update(self):
        first_worker = create_worker("John Doe")
        second_worker = create_worker("Jack Doe")
        created_shift = create_shift(
            first_worker, datetime.datetime.now().date(),
            ShiftDuration.FIRST_SHIFT)
        shift_service = ShiftService()
        updated_shift = shift_service.update(
            second_worker, created_shift.id, datetime.datetime.
            now().date(),
            ShiftDuration.SECOND_SHIFT)
        found_shift = Shift.objects.get(pk=1)
        self.assertEqual(found_shift, updated_shift)

    def test_get(self):
        worker = create_worker("John Doe")
        created_shift = create_shift(
            worker, datetime.datetime.now().date(),
            ShiftDuration.FIRST_SHIFT)
        shift_service = ShiftService()
        found_shift = shift_service.get(created_shift.id)
        self.assertEqual(found_shift, created_shift)

    def test_delete(self):
        worker = create_worker("John Doe")
        created_shift = create_shift(
            worker, datetime.datetime.now().date(),
            ShiftDuration.FIRST_SHIFT)
        shift_service = ShiftService()
        deleted_shift = shift_service.delete(created_shift.id)
        self.assertEqual(deleted_shift.id, None)
