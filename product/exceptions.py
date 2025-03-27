from rest_framework.exceptions import APIException as DRFAPIException
class APIException(DRFAPIException):
    status_code = 404
    default_detail = "Ephraim error when fetching user with id"
    default_code = "custom_error"

    def __init__(self, message=None, status_code=None, code=None, hint=None, extra=None):
        if status_code is not None:
            self.status_code = status_code
            
        self.detail = {
            "error": message or self.default_detail,
            "code": code or self.default_code,
            "hint": hint or "Please check your request and try again.",
            "extra": extra or {}
        }

