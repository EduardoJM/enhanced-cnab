from cnab.base.remessa import Remessa
from .registro0 import BancoBrasil240Registro0
from .registro9 import BancoBrasil240Registro9

class CNAB240BancoBrasil(Remessa):
    header: BancoBrasil240Registro0
    registro0_class = BancoBrasil240Registro0
    registro9_class = BancoBrasil240Registro9

    def inserir_lote(self, **kwargs):
        # TODO: implement kwargs named here
        return super().inserir_lote(**kwargs)
