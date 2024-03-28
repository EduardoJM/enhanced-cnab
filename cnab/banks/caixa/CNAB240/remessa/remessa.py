from cnab.base.remessa import Remessa
from cnab.repository import register_remessa_layout
from .registro0 import Caixa240Registro0
from .registro9 import Caixa240Registro9


@register_remessa_layout("104", "CNAB240")
class CNAB240Caixa(Remessa):
    header: Caixa240Registro0
    registro0_class = Caixa240Registro0
    registro9_class = Caixa240Registro9
