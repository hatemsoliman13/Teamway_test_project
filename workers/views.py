from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from validators.requestvalidator import RequestValidator
from validators.exceptions import RequestValidatorException
from .apps import WorkersConfig
from .services import WorkerService
from .models import Worker
from json.decoder import JSONDecodeError
import json

# Create your views here.


@require_http_methods(["GET"])
def index(request):
    workers = [worker.as_dict() for worker in Worker.objects.all()]
    response = {"status": "Success",
                "result": workers, "error_message": ""}
    return JsonResponse(response)


@require_http_methods(["POST"])
def create(request):
    try:
        data = json.loads(request.body)
        request_validator = RequestValidator(
            data, WorkersConfig.validation_rules[create.__name])
        request_validator.validate_data()

        worker_service = WorkerService()
        worker = worker_service.create(data["name"])

        response = {"status": "Success", "result": [
            worker.as_dict()], "error_message": ""}
    except JSONDecodeError as e:
        response = {
            "status": "Failed", "result": [],
            "error_message": str(e)}
    except RequestValidatorException as e:
        response = {
            "status": "Failed", "result": [],
            "error_message": e.violations}
    except IntegrityError:
        response = {"status": "Failed", "result": [],
                    "error_message": "Worker already exists"}
    return JsonResponse(response)


@require_http_methods(["PATCH"])
def update(request):
    try:
        data = json.loads(request.body)

        request_validator = RequestValidator(
            data, WorkersConfig.validation_rules[update.__name__])
        request_validator.validate_data()

        worker_service = WorkerService()
        worker = worker_service.update(
            data["worker_id"],
            data["name"])

        response = {"status": "Success", "result": [
            worker.as_dict()], "error_message": ""}

    except JSONDecodeError as e:
        response = {"status": "Failed", "result": [],
                    "error_message": str(e)}
    except RequestValidatorException as e:
        response = {
            "status": "Failed", "result": [],
            "error_message": e.violations}
    except ObjectDoesNotExist:
        response = {"status": "Failed", "result": [],
                    "error_message": "Worker does not exist"}
    except IntegrityError:
        response = {"status": "Failed", "result": [],
                    "error_message": "Worker already exists"}
    return JsonResponse(response)


@require_http_methods(["GET"])
def details(request):
    try:
        data = json.loads(request.body)

        request_validator = RequestValidator(
            data, WorkersConfig.validation_rules[details.__name__])
        request_validator.validate_data()

        worker_service = WorkerService()
        worker = worker_service.get(data["worker_id"])

        response = {"status": "Success", "result": [
            worker.as_dict()], "error_message": ""}

    except JSONDecodeError as e:
        response = {"status": "Failed", "result": [],
                    "error_message": str(e)}
    except RequestValidatorException as e:
        response = {"status": "Failed", "result": [],
                    "error_message": e.violations}
    except ObjectDoesNotExist:
        response = {"status": "Failed", "result": [],
                    "error_message": "Worker does not exist"}
    return JsonResponse(response)


@require_http_methods(["DELETE"])
def delete(request):
    try:
        data = json.loads(request.body)

        request_validator = RequestValidator(
            data, WorkersConfig.validation_rules[delete.__name__])
        request_validator.validate_data()

        worker_service = WorkerService()
        worker = worker_service.delete(data["worker_id"])

        response = {
            "status": "Success", "result": [worker.as_dict()],
            "error_message": ""}

    except JSONDecodeError as e:
        response = {"status": "Failed", "result": [],
                    "error_message": str(e)}
    except RequestValidatorException as e:
        response = {
            "status": "Failed", "result": [],
            "error_message": e.violations}
    except ObjectDoesNotExist:
        response = {"status": "Failed", "result": [],
                    "error_message": "Worker does not exist"}
    return JsonResponse(response)
