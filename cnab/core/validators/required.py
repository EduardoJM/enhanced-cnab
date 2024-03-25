from cnab.core.exceptions import CNABFieldValueRequiredError

EMPTY_VALUES = ["", None]

def validate_required(value, field):
    if value in EMPTY_VALUES:
        raise CNABFieldValueRequiredError(field.name)
    return value
