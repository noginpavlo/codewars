"""
Try to implement a design pattern that I liked.
"""

"""
Error codes:
    LogicError - 0
    PerseptionError - 1
"""

# interface
class Error:
    def __init__(self, code: int):
        self.code = code

    @staticmethod
    def meet_condition(code) -> bool:
        return False


# low-level module
class LogicError(Error):
    @staticmethod
    def meet_condition(error_code):
        return error_code == 0


class PerceptionError(Error):
    @staticmethod
    def meet_condition(error_code) -> bool:
        return error_code == 1


class UnknownError(Error):
    """This is Null Object Pattern that returns itself and does nothing."""


# high-level module
class ErrorChecker:

    def __init__(self, error_code: int):
        self.error_code = error_code

    def identify_error_type(self):
        for error_cls in Error.__subclasses__():
            try:
                if error_cls.meet_condition(self.error_code):
                    return error_cls(self.error_code)
            except KeyError:
                continue
        return UnknownError(self.error_code)
