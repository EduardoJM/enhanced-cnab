from .base import FormatterBase


class FormatterDecimal(FormatterBase):
    def to_file(self, value: float):
        value = "%.2f" % round(value, self.field.precision)
        value = value.replace(",", "").replace(".", "")
        value = value.rjust(self.field.length + self.field.precision, "0")
        return value

    def from_file(self, value):
        main = int(value[0 : self.field.length])
        decimal = int(value[-self.field.precision :]) / 100
        return main + decimal
