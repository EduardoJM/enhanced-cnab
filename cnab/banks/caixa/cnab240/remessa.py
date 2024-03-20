from cnab.base.remessa import Remessa
from .registro0 import Caixa240Registro0
from .registro9 import Caixa240Registro9

class CNAB240Caixa(Remessa):
    header: Caixa240Registro0
    registro0_class = Caixa240Registro0
    registro9_class = Caixa240Registro9

