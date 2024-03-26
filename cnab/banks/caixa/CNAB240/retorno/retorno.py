from typing import List, Union
from cnab.base.retorno import Retorno
from .registro0 import CaixaRetornoCnab240Registro0
from .registro9 import CaixaRetornoCnab240Registro9

class CNAB400CaixaRetorno(Retorno):
    registro0_class = CaixaRetornoCnab240Registro0
    registro9_class = CaixaRetornoCnab240Registro9

    children: List[Union[CaixaRetornoCnab240Registro0, CaixaRetornoCnab240Registro9]]
