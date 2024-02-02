from enum import Enum

class TipoServico(Enum):
    Registrado = 1
    SemRegistro = 2

class TipoInscricao(Enum):
    CPF = 1
    CNPJ = 2
