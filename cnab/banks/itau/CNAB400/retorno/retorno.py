from typing import List, Union

from cnab.base.retorno import Retorno
from cnab.repository import register_retorno_layout

from .registro0 import ItauRetornoCnab400Registro0
from .registro9 import ItauRetornoCnab400Registro9


@register_retorno_layout("341", "400")
class CNAB400ItauRetorno(Retorno):
    registro0_class = ItauRetornoCnab400Registro0
    registro9_class = ItauRetornoCnab400Registro9

    children: List[Union[ItauRetornoCnab400Registro0, ItauRetornoCnab400Registro9]]
