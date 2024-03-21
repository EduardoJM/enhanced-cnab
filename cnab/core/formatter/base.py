from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cnab.core.field import CNABField

class FormatterBase(ABC):
    field: "CNABField"

    def __init__(self, field: "CNABField"):
        self.field = field

    @abstractmethod
    def to_file(self, value):
        pass

    @abstractmethod
    def from_file(self, value):
        pass
