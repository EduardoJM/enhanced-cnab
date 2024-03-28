from .base import FormatterBase
from .integer import FormatterInteger
from .alfa import FormatterAlfa


class FormatterEnum(FormatterBase):
    behaviour_integer: bool

    def __init__(self, field, is_integer: bool):
        super().__init__(field)
        self.behaviour_integer = is_integer

    def to_file(self, value):
        if self.behaviour_integer:
            return FormatterInteger(self.field).to_file(value)
        return FormatterAlfa(self.field).to_file(value)

    def from_file(self, value):
        raise NotImplementedError("TODO: implements this.")
