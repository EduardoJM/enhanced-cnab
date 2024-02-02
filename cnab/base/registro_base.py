from abc import ABC, abstractmethod
from typing import List, Optional
from cnab.core.field import CNABField
from cnab.core import exceptions

class RegistroBase(ABC):
    _children: List["RegistroBase"] = []
    _meta: Optional[dict] = None
    _data: Optional[dict] = None

    def __init__(self, **kwargs: dict):
        self._data = kwargs

    def get_field(self, key: str) -> CNABField:
        item = self._meta[key]
        if not isinstance(item, CNABField):
            raise exceptions.IsNotCNABFieldError(key)
        item.name = key
        return item

    def get_value(self, key, default):
        value = None

        if hasattr(self, f'get_{key}'):
            fn = getattr(self, f'get_{key}')
            value = fn()

        if not value:
            value = self._data.get(key, default)

        field = self.get_field(key)
        return field.format_value(value)

    def append(self, child: "RegistroBase"):
        self._children.append(child)

    @abstractmethod
    def get_text(self) -> str:
        raise NotImplementedError("get_text() is not implemented")
