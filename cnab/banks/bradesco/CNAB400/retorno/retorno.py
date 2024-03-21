from cnab.base.retorno import Retorno
from .registro0 import BradescoRetornoCnab400Registro0
from .registro9 import BradescoRetornoCnab400Registro9

class CNAB400BradescoRetorno(Retorno):
    registro0_class = BradescoRetornoCnab400Registro0
    registro9_class = BradescoRetornoCnab400Registro9
