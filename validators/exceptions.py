class RequestValidatorException(Exception):
    def __init__(self, *args, **kwargs) -> None:
        self.violations = kwargs["violations"]
