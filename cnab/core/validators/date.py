from cnab.core.exceptions import IsNotValidDateTimeError

def validate_date(value, field):
    if not hasattr(value, 'strftime'):
        raise IsNotValidDateTimeError(field.name)
    return value
