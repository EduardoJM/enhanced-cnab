from cnab.base.remessa import Remessa
from cnab.repository import register_remessa_layout
from .registro0 import BradescoCnab400Registro0
from .registro9 import BradescoCnab400Registro9


@register_remessa_layout("237", "CNAB400")
class CNAB400Bradesco(Remessa):
    header: BradescoCnab400Registro0
    registro0_class = BradescoCnab400Registro0
    registro9_class = BradescoCnab400Registro9

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def inserir_lote(self, **kwargs) -> "BradescoCnab400Registro0":
        return super().inserir_lote(**kwargs)
