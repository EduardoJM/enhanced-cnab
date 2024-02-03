from cnab.core.exceptions import IsNotValidDateTimeError

def validate_date(value, field):
    if value == '0':
        return value
    if not hasattr(value, 'strftime'):
        raise IsNotValidDateTimeError(field.name)
    return value
