from django.test import TestCase
from .requestvalidator import RequestValidator
from .exceptions import RequestValidatorException


class RequestValidatorTests(TestCase):
    request_data = {"name": 123, "worker_id": "",
                    "sift_id": 4, "duration": "00-18"}
    validatation_rules = {
        "name": {"required": True, "type": str},
        "worker_id": {"required": True},
        "shift_id": {"required": True},
        "duration":
        {"required": True, "values": ["00-08", "08-16", "16-24"]}}

    def test_validate_data(self):
        expected_violations = [
            "(name) has incorrect type, it should be (<class 'str'>)",
            '(worker_id) should not be empty)',
            'Missing (shift_id) from request)',
            'Incorrect Value for (duration)']

        request_validator = RequestValidator(
            self.request_data, self.validatation_rules)
        try:
            request_validator.validate_data()
        except RequestValidatorException as e:
            self.assertEqual(expected_violations, e.violations)
