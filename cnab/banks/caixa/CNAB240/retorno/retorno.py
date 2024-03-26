from typing import List, Union
from cnab.base.retorno import Retorno
from cnab.repository import register_retorno_layout
from .registro0 import CaixaRetornoCnab240Registro0
from .registro9 import CaixaRetornoCnab240Registro9

@register_retorno_layout('104', '040')
class CNAB400CaixaRetorno(Retorno):
    registro0_class = CaixaRetornoCnab240Registro0
    registro9_class = CaixaRetornoCnab240Registro9

    children: List[Union[CaixaRetornoCnab240Registro0, CaixaRetornoCnab240Registro9]]
