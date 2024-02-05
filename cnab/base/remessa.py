from typing import List
from .layouts.CNAB240.Registro0 import CNAB240Registro0

class Remessa:
    header: CNAB240Registro0
    registro0_class = None
    registro9_class = None

    def __init__(self, **kwargs):
        self.header = self.registro0_class(**kwargs)

    def inserir_lote(self, **kwargs):
        return self.header.inserir_lote(**kwargs)

    def get_text(self) -> List[str]:
        footer = self.registro9_class(self.header, None, **{ '1': 1 })
        return self.header.get_text() + footer.get_text()
