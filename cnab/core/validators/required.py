from cnab.core.exceptions import CNABFieldValueRequiredError

def validate_required(value, field):
    if not value:
        raise CNABFieldValueRequiredError(field.name)
    return value
