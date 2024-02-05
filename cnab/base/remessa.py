from typing import List
from abc import ABC
from .cnab_240.registro0 import CNAB240Registro0

class Remessa(ABC):
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
