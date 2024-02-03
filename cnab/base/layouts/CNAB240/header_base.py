from typing import Optional
from cnab.base.registro_base import RegistroBase
from cnab.base.registro_remessa import RegistroRemessa
from datetime import datetime

class CNAB240HeaderBase(RegistroRemessa):
    def __init__(
        self,
        header: Optional[RegistroBase],
        parent: Optional[RegistroBase],
        **kwargs: dict
    ):
        self.counter = 0
        super().__init__(header, parent, **kwargs)

    def get_data_geracao(self):
        return datetime.now()
    
    def get_hora_geracao(self):
        return datetime.now()
    
    def append(self, child: RegistroBase):
        super().append(child)
        self.counter += 1
