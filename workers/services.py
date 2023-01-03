from .models import Worker


class WorkerService():

    def create(self, name: str):
        worker = Worker(name=name)
        worker.save()
        return worker

    def update(self, worker_id: int, name: str):
        worker = self.get(worker_id)
        worker.name = name
        worker.save()
        return worker

    def get(self, worker_id: int):
        return Worker.objects.get(pk=worker_id)

    def delete(self, worker_id: int):
        worker = self.get(worker_id)
        worker.delete()
        return worker
