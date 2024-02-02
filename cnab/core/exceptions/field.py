
class CNABFieldValueRequiredError(Exception):
    def __init__(self, field_name: str):
        msg = f"Field not found or field with empty value: {field_name}"
        super().__init__(msg)

class CNABFieldNotIntegerError(Exception):
    def __init__(self, field_name: str):
        msg = f"The Integer field value is not parseable to int: {field_name}"
        super().__init__(msg)

class CNABFieldNotDecimalError(Exception):
    def __init__(self, field_name: str):
        msg = f"The decimal field value is not parseable to float: {field_name}"
        super().__init__(msg)

class CNABFieldTypeNotSupportedError(Exception):
    def __init__(self, field_type: str):
        msg = f"The field type {field_type} is not supported."
        super().__init__(msg)

class IsNotCNABFieldError(Exception):
    def __init__(self, field_name: str):
        msg = f"The meta field is not a CNABField instance: {field_name}"
        super().__init__(msg)

class IsNotValidDateTimeError(Exception):
    def __init__(self, field_name: str):
        msg = f"The date or time field needs an instance with strftime function: {field_name}"
        super().__init__(msg)
