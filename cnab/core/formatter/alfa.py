from unidecode import unidecode
from .base import FormatterBase

class FormatterAlfa(FormatterBase):
    def prepare_text(self, text: str) -> str:
        return unidecode(text.strip()).upper()
    
    def to_file(self, value):
        value = self.prepare_text(str(value))
        if len(value) > self.field.length:
            value = value[0:self.field.length]
        return value.ljust(self.field.length, ' ')
    
    def from_file(self, value):
        return str(value).strip()
