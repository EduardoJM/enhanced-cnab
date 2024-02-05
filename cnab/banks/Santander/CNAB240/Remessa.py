from cnab.base.remessa import Remessa
from .Registro0 import Santander240Registro0
from .Registro9 import Santander240Registro9

class CNAB240Santander(Remessa):
    header: Santander240Registro0
    registro0_class = Santander240Registro0
    registro9_class = Santander240Registro9

    def inserir_lote(self, **kwargs):
        # TODO: implement kwargs named here
        super().inserir_lote(**kwargs)
