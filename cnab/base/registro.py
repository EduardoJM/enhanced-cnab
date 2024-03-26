from abc import abstractmethod
from typing import List, Optional
from cnab.core.field import CNABField
from cnab.core.registro import RegistroBase
from cnab.core import exceptions

class Registro(RegistroBase):
    parent: Optional["Registro"] = None
    header: Optional["Registro"] = None

    _children: List["Registro"] = []
    _meta: Optional[dict] = None

    def __init__(self, header: Optional["Registro"], parent: Optional["Registro"], **kwargs: dict):
        self.header = header
        self._children = []
        self.parent = parent
        
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        if not parent:
            return
        parent.append(self)


    def get_field(self, key: str) -> CNABField:
        # TODO: remove this
        item = self._meta[key]
        if not isinstance(item, CNABField):
            raise exceptions.IsNotCNABFieldError(key)
        item.name = key
        return item

    def get_codigo_carteira(self):
        if not hasattr(self, 'codigo_carteira'):
            return None
        value = self.codigo_carteira
        if not value:
            return None
        return int(value)

    def append(self, child: "Registro"):
        self._children.append(child)

    @abstractmethod
    def get_text(self) -> str:
        raise NotImplementedError("get_text() is not implemented")
