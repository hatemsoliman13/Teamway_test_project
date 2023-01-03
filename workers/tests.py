from django.test import TestCase
from .services import WorkerService
from .models import Worker

# Create your tests here.


def create_worker(name: str) -> Worker:
    worker = Worker(name=name)
    worker.save()
    return worker


class WorkerServiceTests(TestCase):
    def test_create(self):
        worker_service = WorkerService()
        created_worker = worker_service.create("Jack Doe")
        existing_worker = Worker.objects.get(pk=1)
        self.assertEqual(created_worker,  existing_worker)

    def test_update(self):
        created_worker = create_worker("Jack Doe")
        worker_service = WorkerService()
        updated_worker = worker_service.update(
            created_worker.id, "John Miller")
        found_worker = Worker.objects.get(pk=1)
        self.assertEqual(updated_worker, found_worker)

    def test_get(self):
        created_worker = create_worker("Jack Doe")
        worker_service = WorkerService()
        found_worker = worker_service.get(created_worker.id)
        self.assertEqual(found_worker, created_worker)

    def test_delete(self):
        created_worker = create_worker("Jack Doe")
        worker_service = WorkerService()
        deleted_worker = worker_service.delete(created_worker.id)
        self.assertEqual(deleted_worker.id, None)
