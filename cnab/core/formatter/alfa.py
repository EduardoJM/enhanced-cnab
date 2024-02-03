import re
from unidecode import unidecode

def remove_accents(text: str) -> str:
    regexes = [
        r'\xc3[\x80-\x85]',
        r'\xc3\x87',
        r'\xc3[\x88-\x8b]',
        r'\xc3[\x8c-\x8f]',
        r'\xc3([\x92-\x96]|\x98)',
        r'\xc3[\x99-\x9c]',
        r'\xc3[\xa0-\xa5]',
        r'\xc3\xa7',
        r'\xc3[\xa8-\xab]',
        r'\xc3[\xac-\xaf]',
        r'\xc3([\xb2-\xb6]|\xb8)',
        r'\xc3[\xb9-\xbc]'
    ]
    replacers = ['A', 'C', 'E', 'I', 'O', 'U', 'a', 'c', 'e', 'i', 'o', 'u']
    for regex, repl in zip(regexes, replacers):
        text = re.sub(regex, repl, text).lower()
    return text

def prepare_text(text: str) -> str:
    return unidecode(text.strip()).upper()
    return remove_accents(text.strip()).upper()

def format_alfa(value, field):
    value = prepare_text(str(value))
    if len(value) > field.length:
        value = value[0:field.length]
    return value.ljust(field.length, ' ')
