from abc import ABC, abstractmethod
from typing import List, Optional
from cnab.core.field import CNABField
from cnab.core import exceptions

class RegistroBase(ABC):
    parent: Optional["RegistroBase"] = None
    header: Optional["RegistroBase"] = None

    _children: List["RegistroBase"] = []
    _meta: Optional[dict] = None
    _data: Optional[dict] = None

    def __init__(self, header: Optional["RegistroBase"], parent: Optional["RegistroBase"], **kwargs: dict):
        self.header = header
        self._children = []
        self.parent = parent
        self._data = kwargs

    def get_field(self, key: str) -> CNABField:
        item = self._meta[key]
        if not isinstance(item, CNABField):
            raise exceptions.IsNotCNABFieldError(key)
        item.name = key
        return item

    def get_unformated(self, key, default=None):
        value = None
        if hasattr(self, f'get_{key}'):
            fn = getattr(self, f'get_{key}')
            value = fn()

        if not value:
            value = self._data.get(key, default)
        return value

    def get_value(self, key, default=None):
        value = self.get_unformated(key, default)
        field = self.get_field(key)
        return field.format_value(value)
    
    def get_data_or_parent(self, field: str):
        if self._data.get(field):
            return self._data.get(field)
        if not self.header:
            return None
        return self.header._data.get(field)

    def get_codigo_carteira(self):
        value = self._data.get('codigo_carteira')
        if not value:
            return None
        return int(value)

    def append(self, child: "RegistroBase"):
        self._children.append(child)

    @abstractmethod
    def get_text(self) -> str:
        raise NotImplementedError("get_text() is not implemented")
