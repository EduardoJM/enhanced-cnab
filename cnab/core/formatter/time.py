from datetime import datetime
from .base import FormatterBase


class FormatterTime(FormatterBase):
    def to_file(self, value: datetime):
        if value == "0":
            return value * 6
        return value.strftime("%H%M%S")

    def from_file(self, value):
        return datetime.strptime(value, "%H%M%S").time()
