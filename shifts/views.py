from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from validators.requestvalidator import RequestValidator
from validators.exceptions import RequestValidatorException
from workers.services import WorkerService
from .models import Shift
from .apps import ShiftsConfig
from .services import ShiftService
from json.decoder import JSONDecodeError
import datetime
import json
# Create your views here.


@require_http_methods(["GET"])
def index(request):
    shifts = [
        shift.as_dict()
        for shift in Shift.objects.filter(
            date__gte=datetime.date.today())]
    response = {"status": "Success",
                "result": shifts, "error_message": ""}
    return JsonResponse(response)


@require_http_methods(["POST"])
def create(request):
    try:
        data = json.loads(request.body)
        data["date"] = datetime.datetime.strptime(
            data["date"], "%d-%m-%Y").date()

        request_validator = RequestValidator(
            data, ShiftsConfig.validation_rules[create.__name__])
        request_validator.validate_data()

        worker_service = WorkerService()
        worker = worker_service.get(data["worker_id"])

        shift_service = ShiftService()
        shift = shift_service.create(
            data['date'],
            worker, data["duration"])

        response = {"status": "Success", "result": [
            shift.as_dict()], "error_message": ""}

    except JSONDecodeError as e:
        response = {"status": "Failed", "result": [],
                    "error_message": str(e)}
    except KeyError:
        response = {"status": "Failed", "result": [
        ], "error_message": "Shift date is missing from request"}
    except ValueError:
        response = {"status": "Failed", "result": [
        ], "error_message": "Invalid date format, please use this format (%d-%m-%Y)"}
    except RequestValidatorException as e:
        response = {
            "status": "Failed", "result": [],
            "error_message": e.violations}
    except ObjectDoesNotExist:
        response = {"status": "Failed", "result": [],
                    "error_message": "Worker does not exist"}
    except IntegrityError:
        response = {"status": "Failed", "result": [],
                    "error_message": "Worker already have a shift"}
    return JsonResponse(response)


@require_http_methods(["PATCH"])
def update(request):
    try:
        data = json.loads(request.body)
        data["date"] = datetime.datetime.strptime(
            data["date"], "%d-%m-%Y").date()

        request_validator = RequestValidator(
            data, ShiftsConfig.validation_rules[update.__name__])
        request_validator.validate_data()

        worker_service = WorkerService()
        worker = worker_service.get(data["worker_id"])

        shift_service = ShiftService()
        shift = shift_service.update(
            worker, data["shift_id"],
            data["date"],
            data["duration"])

        response = {"status": "Success", "result": [
            shift.as_dict()], "error_message": ""}
    except JSONDecodeError as e:
        response = {"status": "Failed", "result": [],
                    "error_message": str(e)}
    except KeyError:
        response = {"status": "Failed", "result": [
        ], "error_message": "Shift date is missing from request"}
    except ValueError:
        response = {"status": "Failed", "result": [
        ], "error_message": "Invalid date format, please use this format (%d-%m-%Y)"}
    except RequestValidatorException as e:
        response = {
            "status": "Failed", "result": [],
            "error_message": e.violations}
    except ObjectDoesNotExist:
        response = {"status": "Failed", "result": [],
                    "error_message": "shift does not exist"}
    except IntegrityError:
        response = {"status": "Failed", "result": [],
                    "error_message": "Worker already have a shift"}
    return JsonResponse(response)


@require_http_methods(["GET"])
def details(request):
    try:
        data = json.loads(request.body)

        request_validator = RequestValidator(
            data, ShiftsConfig.validation_rules[details.__name__])
        request_validator.validate_data()

        shift_service = ShiftService()
        shift = shift_service.get(data["shift_id"])

        response = {"status": "Success", "result": [
            shift.as_dict()], "error_message": ""}
    except JSONDecodeError as e:
        response = {"status": "Failed", "result": [],
                    "error_message": str(e)}
    except RequestValidatorException as e:
        response = {
            "status": "Failed", "result": [],
            "error_message": e.violations}
    except ObjectDoesNotExist:
        response = {"status": "Failed", "result": [],
                    "error_message": "Shift does not exist"}
    return JsonResponse(response)


@require_http_methods(["DELETE"])
def delete(request):
    try:
        data = json.loads(request.body)

        request_validator = RequestValidator(
            data, ShiftsConfig.validation_rules[delete.__name__])
        request_validator.validate_data()

        shift_service = ShiftService()
        shift = shift_service.delete(data["shift_id"])

        response = {
            "status": "Success", "result": [shift.as_dict()],
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
                    "error_message": "Shift does not exist"}
    return JsonResponse(response)
