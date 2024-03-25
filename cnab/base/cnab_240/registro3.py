from typing import Optional
from cnab.base.registro_remessa import RegistroRemessa
from cnab.base.registro import Registro
from cnab.core.especie import EspecieTitulo
from .registro1 import CNAB240Registro1

class CNAB240Registro3(RegistroRemessa):
    lote: CNAB240Registro1 = None

    def __init__(self,
        header: Optional["Registro"],
        parent: Optional["Registro"],
        lote: CNAB240Registro1,
        **kwargs: dict,
    ):
        self.lote = lote
        super().__init__(header, parent, **kwargs)
        self.init_numero_registro()

    def init_numero_registro(self):
        self.numero_registro = self.lote.counter

    def get_seu_numero2(self):
        # TODO: remove this???
        value = self.seu_numero2
        if value:
            return value
        
        if hasattr(self, 'get_nosso_numero'):
            return self.get_nosso_numero()
        
        return self.nosso_numero
    
    def append(self, child: Registro):
        super().append(child)
        self.lote.counter += 1

    def get_especie_titulo(self):
        # TODO: rewrite this function
        codigo_banco = self.get_field('codigo_banco')
        return EspecieTitulo.get_real_value(
            codigo_banco.default,
            self.especie_titulo
        )
    