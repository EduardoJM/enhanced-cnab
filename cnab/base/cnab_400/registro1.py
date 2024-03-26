from typing import Optional
from datetime import datetime
from cnab.base.registro_remessa import RegistroRemessa
from cnab.base.registro import Registro
from cnab.core.especie import EspecieTitulo

class CNAB400Registro1(RegistroRemessa):
    def __init__(self, header: Optional["Registro"], parent: Optional["Registro"], **kwargs: dict):
        super().__init__(header, parent, **kwargs)
        self.init_numero_registro()

    def init_numero_registro(self):
        if hasattr(self, 'numero_registro'):
            self.numero_registro = self.header.counter
        if hasattr(self, 'numero_sequencial'):
            self.numero_sequencial = self.header.counter

    def append(self, child: Registro):
        super().append(child)

        self.header.counter += 1
    
    #def get_especie_titulo(self):
    #    field = self.header.get_field('codigo_banco')
    #    return EspecieTitulo.get_real_value(
    #        field.default,
    #        self.especie_titulo,
    #    )
