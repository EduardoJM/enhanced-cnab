from typing import Optional
from cnab.base.registro_base import RegistroBase
from cnab.base.registro_remessa import RegistroRemessa
from cnab.base.layouts.CNAB240 import CNAB240LoteBase

class CNAB240RegistrosBase(RegistroRemessa):
    lote: CNAB240LoteBase = None

    def __init__(self,
        header: Optional["RegistroBase"],
        parent: Optional["RegistroBase"],
        lote: CNAB240LoteBase,
        **kwargs: dict,
    ):
        self.lote = lote
        super().__init__(header, parent, **kwargs)

    def get_qtd_registros(self):
        return self.lote.counter + 2
