from abc import ABC
from typing import Optional, Dict
from cnab.core.field import CNABField

class RegistroRetorno (ABC):
    line: str = ''
    position: int = 0
    _meta: Optional[Dict[str, CNABField]] = None

    def _get_field_value(self, field: CNABField):
        field_length = field.get_real_length()
        value = self.line[self.position, self.position + field_length]
        self.position = self.position + field_length
        return value
    
    def _parse_field(self, key: str, field: CNABField):
        value = self._get_field_value(field)
        setattr(self, key, value)

    def _parse_line(self):
        for key, field in self._meta.items():
            self._parse_field(key, field)

    def __init__(self, line: str):
        self.line = line
        self.position = 0

        self._parse_line()
