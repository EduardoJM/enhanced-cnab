from cnab.core.exceptions import CNABFieldNotDecimalError

def validate_decimal(value, field):
    try:
        value = float(str(value))
    except Exception:
        raise CNABFieldNotDecimalError(field.name)
    return value
