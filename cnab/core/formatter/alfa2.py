def format_alfa2(value, field):
    value = str(value)
    if len(value) > field.length:
        value = value[0:field.length]
    return value.ljust(field.length, ' ')
