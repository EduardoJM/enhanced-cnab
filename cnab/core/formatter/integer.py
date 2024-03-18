def format_integer(value: int, field):
    value = str(value).rjust(field.length, '0')
    if len(value) > field.length:
        value = value[0:field.length]
    return value
