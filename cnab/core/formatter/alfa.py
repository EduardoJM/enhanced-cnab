from unidecode import unidecode

def prepare_text(text: str) -> str:
    return unidecode(text.strip()).upper()

def format_alfa(value, field):
    value = prepare_text(str(value))
    if len(value) > field.length:
        value = value[0:field.length]
    return value.ljust(field.length, ' ')
