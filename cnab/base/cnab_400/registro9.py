from typing import Optional
from cnab.base.registro import Registro
from cnab.base.registro_remessa import RegistroRemessa

class CNAB400Registro9(RegistroRemessa):
    def __init__(self, header: Optional[Registro], parent: Optional[Registro], **kwargs: dict):
        super().__init__(header, parent, **kwargs)
        
        self.init_numero_registro()

    def init_numero_registro(self):
        self._data['numero_registro'] = self.header.counter + 1
        self._data['numero_sequencial'] = self.header.counter + 1
