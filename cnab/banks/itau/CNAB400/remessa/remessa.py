from typing import TYPE_CHECKING
from cnab.base.remessa import Remessa
from cnab.repository import register_remessa_layout
from .registro0 import ItauCnab400Registro0
from .registro9 import ItauCnab400Registro9

if TYPE_CHECKING:
    from .registro0 import ItauCnab400Registro0


@register_remessa_layout("341", "CNAB400")
class CNAB400Itau(Remessa):
    header: ItauCnab400Registro0
    registro0_class = ItauCnab400Registro0
    registro9_class = ItauCnab400Registro9

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def inserir_lote(self, **kwargs) -> "ItauCnab400Registro0":
        return super().inserir_lote(**kwargs)
