from abc import abstractmethod
from typing import List, Optional, Callable
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

    #def get_unformated(self, key, default=None):
    #    value = None
    #    if hasattr(self, f'get_{key}'):
    #        fn = getattr(self, f'get_{key}')
    #        value = fn()
    #
    #    if not value:
    #        value = getattr(self, key)
    #
    #    if not value:
    #        return default
    #    return value
    
    #def get_default(self, field: CNABField):
    #    print(field)
    #    print(field.default)
    #
    #    if not field.default:
    #        return field.default
    #    
    #    if isinstance(field.default, Callable):
    #        return field.default()
    #    
    #    return field.default

    #def get_value(self, key, default=None):
    #    value = self.get_unformated(key, default)
    #    field = self.get_field(key)
    #    print("@@@@@@@@@@@@@@@@")
    #    print(key)
    #    print(default)
    #    print(value)
    #    return field.format_value(value)

    def get_data_or_parent(self, field: str):
        value = getattr(self, field)
        if value:
            return value
        if not self.header:
            return None
        
        try:
            return getattr(self.header, field)
        except AttributeError:
            return None

    def get_codigo_carteira(self):
        print(dir(self))
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
