def format_integer(value: int, field):
    return str(value).rjust(field.length, '0')
