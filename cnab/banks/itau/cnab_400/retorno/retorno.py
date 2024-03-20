from cnab.base.retorno import Retorno
from .registro0 import ItauRetornoCnab400Registro0

class CNAB400ItauRetorno(Retorno):
    registro0_class = ItauRetornoCnab400Registro0
