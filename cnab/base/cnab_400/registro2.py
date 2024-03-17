from cnab.base.registro import Registro
from cnab.base.registro_remessa import RegistroRemessa

class CNAB400Registro2(RegistroRemessa):
    def __init__(self, header: Registro | None, parent: Registro | None, **kwargs: dict):
        super().__init__(header, parent, **kwargs)
        
        self.init_numero_registro()

    def init_numero_registro(self):
        self._data['numero_registro'] = self.header.counter
        self._data['numero_sequencial'] = self.header.counter

