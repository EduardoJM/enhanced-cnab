from .base import FormatterBase

class FormatterInteger(FormatterBase):
    def to_file(self, value):
        value = str(value).rjust(self.field.length, '0')
        if len(value) > self.field.length:
            value = value[0:self.field.length]
        return value
    
    def from_file(self, value):
        try:
            return int(value)
        except ValueError:
            return value
