from typing import Optional
from cnab.core.field import CNABFieldEnum
from .enum import EspecieTitulo

class CNABFieldEspecieTitulo(CNABFieldEnum[EspecieTitulo]):
    def __init__(
        self,
        segment: str,
        length: int,
        required: Optional[bool] = False,
    ):
        super().__init__(
            EspecieTitulo,
            segment,
            length,
            EspecieTitulo.DuplicataMercantil,
            required,
            is_integer=True
        )

    def validate_value(self, value):
        field_codigo_banco = self.registro.header.get_field('codigo_banco')
        value = EspecieTitulo.get_real_value(
            field_codigo_banco.default,
            value,
        )
        
        for validator in self.validators:
            value = validator(value, self)

        return value

__all__ = ['CNABFieldEspecieTitulo']
