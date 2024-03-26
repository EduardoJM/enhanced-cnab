from typing import Optional, List
from cnab.core.field import CNABField
from cnab.core.registro import RegistroBase
from cnab.core import exceptions

class RegistroRemessa(RegistroBase):
    parent: Optional["RegistroRemessa"] = None
    header: Optional["RegistroRemessa"] = None

    _children: List["RegistroRemessa"] = []
    _meta: Optional[dict] = None

    def __init__(self, header: Optional["RegistroRemessa"], parent: Optional["RegistroRemessa"], **kwargs: dict):
        self.header = header
        self._children = []
        self.parent = parent
        
        setted = []
        for key, value in kwargs.items():
            setted = [*setted, key]
            setattr(self, key, value)

        for key, field in self._meta.items():
            if key in setted:
                continue
            if field.auto_generated:
                continue
            value = field.get_value_default()
            if value is None:
                continue
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

    def append(self, child: "RegistroRemessa"):
        self._children.append(child)

    def get_text(self) -> str:
        retorno = ''
        for _, field in self._meta.items():
            retorno += field.get_value()
            
        result = [retorno]

        for child in self._children:
            result += child.get_text()

        return result
