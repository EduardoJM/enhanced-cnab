def format_decimal(value: float, field):
    value = str(round(value, field.precision)).replace(',', '').replace('.', '')
    value = value.rjust(field.length + field.precision, '0')
    return value
