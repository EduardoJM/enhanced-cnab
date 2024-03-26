from cnab.base.remessa import Remessa
from cnab.repository import register_remessa_layout
from .registro0 import Santander240Registro0
from .registro9 import Santander240Registro9

@register_remessa_layout('033', 'CNAB240')
class CNAB240Santander(Remessa):
    header: Santander240Registro0
    registro0_class = Santander240Registro0
    registro9_class = Santander240Registro9

    def inserir_lote(self, **kwargs):
        # TODO: implement kwargs named here
        return super().inserir_lote(**kwargs)
