from cnab.base.registro_base import RegistroBase
from cnab.base.registro_remessa import RegistroRemessa
from datetime import datetime
from .Registro3 import CNAB240Registro3

class CNAB240Registro0(RegistroRemessa):
    registro1_class = None

    def __init__(
        self,
        **kwargs: dict
    ):
        self.counter = 0
        super().__init__(None, None, **kwargs)

    def get_data_geracao(self):
        return datetime.now()
    
    def get_hora_geracao(self):
        return datetime.now()
    
    def append(self, child: RegistroBase):
        super().append(child)
        self.counter += 1

    def inserir_lote(self, **kwargs: dict) -> CNAB240Registro3:
        if not hasattr(self, 'registro1_class'):
            raise Exception("TODO: better exception here")
        if not self.registro1_class:
            raise Exception("TODO: better exception here")
        
        return self.registro1_class(self, self, **kwargs)
