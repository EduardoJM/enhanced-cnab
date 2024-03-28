from cnab.base.retorno import Retorno
from cnab.repository import register_retorno_layout

from .registro0 import BradescoRetornoCnab400Registro0
from .registro9 import BradescoRetornoCnab400Registro9


@register_retorno_layout("237", "400")
class CNAB400BradescoRetorno(Retorno):
    registro0_class = BradescoRetornoCnab400Registro0
    registro9_class = BradescoRetornoCnab400Registro9
