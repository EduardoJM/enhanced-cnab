from .base import FormatterBase


class FormatterAlfa2(FormatterBase):
    def to_file(self, value):
        value = str(value)
        if len(value) > self.field.length:
            value = value[0 : self.field.length]
        return value.ljust(self.field.length, " ")

    def from_file(self, value):
        return str(value).strip()
