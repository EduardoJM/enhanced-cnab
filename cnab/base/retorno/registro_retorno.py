from typing import Dict, List, Optional

from cnab.core.field import CNABField
from cnab.core.registro import RegistroBase

from .retorno import Retorno


class RegistroRetorno(RegistroBase):
    line: str = ""
    position: int = 0
    file: Retorno
    _meta: Optional[Dict[str, CNABField]] = None
    children: List["RegistroRetorno"] = []

    def _get_field_value(self, field: CNABField):
        field_length = field.get_real_length()
        value = self.line[self.position : self.position + field_length]
        self.position = self.position + field_length
        return value

    def _parse_field(self, key: str, field: CNABField):
        value = self._get_field_value(field)
        value = field.value_from_file(value)
        setattr(self, key, value)

    def _parse_line(self):
        for key, field in self._meta.items():
            self._parse_field(key, field)

    def __init__(self, file: Retorno, line: str):
        self.children = []
        self.file = file
        self.line = line
        self.position = 0

        self._parse_line()
