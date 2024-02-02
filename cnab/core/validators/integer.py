from cnab.core.exceptions import CNABFieldNotIntegerError

def validate_integer(value, field):
    try:
        value = int(str(value))
    except Exception:
        raise CNABFieldNotIntegerError(field.name)
    return value
