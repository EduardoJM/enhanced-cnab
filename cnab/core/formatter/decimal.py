def format_decimal(value: float, field):
    print("#### ", field.name)

    value = "%.2f" % round(value, field.precision)
    if field.name == 'vlr_juros':
        print(value)
    value = value.replace(',', '').replace('.', '')
    if field.name == 'vlr_juros':
        print(value)
    value = value.rjust(field.length + field.precision, '0')
    if field.name == 'vlr_juros':
        print(len(value))

    return value
