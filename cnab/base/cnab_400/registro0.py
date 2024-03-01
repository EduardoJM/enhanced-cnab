from cnab.base.registro import Registro
from cnab.base.registro_remessa import RegistroRemessa
from datetime import datetime
from .registro1 import CNAB400Registro1

class CNAB400Registro0(RegistroRemessa):
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
    
    def append(self, child: Registro):
        super().append(child)
        self.counter += 1
    
    def get_data_gravacao(self):
        return datetime.now()

    def inserir_lote(self, **kwargs: dict) -> CNAB400Registro1:
        if not hasattr(self, 'registro1_class'):
            raise Exception("TODO: better exception here")
        if not self.registro1_class:
            raise Exception("TODO: better exception here")
        
        return self.registro1_class(self, self, **kwargs)
