from typing import Optional
from cnab.base.registro import Registro
from cnab.base.registro_remessa import RegistroRemessa

class CNAB400Registro2(RegistroRemessa):
    def __init__(self, header: Optional[Registro], parent: Optional[Registro], **kwargs: dict):
        super().__init__(header, parent, **kwargs)
        
        self.init_numero_registro()

    def init_numero_registro(self):
        if hasattr(self, 'numero_registro'):
            self.numero_registro = self.header.counter
        if hasattr(self, 'numero_sequencial'):
            self.numero_sequencial = self.header.counter

