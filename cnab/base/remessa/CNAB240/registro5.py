from typing import Optional

from cnab.base.remessa import RegistroRemessa

from .registro1 import CNAB240Registro1


class CNAB240Registro5(RegistroRemessa):
    lote: CNAB240Registro1 = None

    def __init__(
        self,
        header: Optional[RegistroRemessa],
        parent: Optional[RegistroRemessa],
        lote: CNAB240Registro1,
        **kwargs: dict,
    ):
        self.lote = lote
        super().__init__(header, parent, **kwargs)

    def get_qtd_registros(self):
        return self.lote.counter + 2
