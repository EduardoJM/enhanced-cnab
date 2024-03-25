from typing import List, Union
from cnab.base.retorno import Retorno
from .registro0 import ItauRetornoCnab400Registro0
from .registro9 import ItauRetornoCnab400Registro9

class CNAB400ItauRetorno(Retorno):
    registro0_class = ItauRetornoCnab400Registro0
    registro9_class = ItauRetornoCnab400Registro9

    children: List[Union[ItauRetornoCnab400Registro0, ItauRetornoCnab400Registro9]]
