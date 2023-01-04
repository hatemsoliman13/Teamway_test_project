from .exceptions import RequestValidatorException


class RequestValidator():

    def __init__(
            self, data: dict, request_validation_rules: dict) -> None:
        self.data = data
        self.request_validation_rules = request_validation_rules
        self.__violations = []

    def validate_data(self) -> None:
        for key, validation_rules in self.request_validation_rules.items():
            self.__validate_key(key, validation_rules)
        if not self.__is_valid():
            raise RequestValidatorException(
                violations=self.__get_violations())

    def __get_violations(self) -> dict:
        return self.__violations

    def __is_valid(self) -> bool:
        return len(self.__violations) == 0

    def __validate_key(self, key, validation_rules) -> None:
        for flag, value in validation_rules.items():
            if flag == "required" and value == True:
                self.__check_existence(key)
            if flag == "type":
                self.__check_correct_type(key, value)
            if flag == "values":
                self.__check_correct_value(key, value)

    def __check_existence(self, key: str) -> None:
        if not self.__is_key_in_data(key):
            self.__report_violation(
                "Missing ({key}) from request)".format(key=key))
        elif self.__is_empty(key):
            self.__report_violation(
                "({key}) should not be empty)".format(key=key))

    def __check_correct_type(self, key, type) -> None:
        if self.__is_key_in_data(key) and not self.__has_correct_type(
                key, type):
            self.__report_violation(
                "({key}) has incorrect type, it should be ({correct_type})".
                format(key=key, correct_type=type))

    def __check_correct_value(self, key, values) -> None:
        if self.__is_key_in_data(key) and not self.__has_correct_value(
                key, values):
            self.__report_violation(
                "Incorrect Value for ({key})".format(key=key))

    def __report_violation(self, violation: str) -> None:
        self.__violations.append(violation)

    def __is_key_in_data(self, key: str) -> bool:
        return key in self.data

    def __is_empty(self, key: str) -> bool:
        return not bool(self.data[key])

    def __has_correct_type(self, key: str, type: type) -> bool:
        return isinstance(self.data[key], type)

    def __has_correct_value(self, key: str, values: list) -> bool:
        return self.data[key] in values
