from typing import Optional, Union
from cnab.base.cnab_400 import CNAB400Registro0
from cnab.core.field import CNABField, CNABFieldType
from cnab.utils.dict_utils import set_if_has_value
# from .registro1 import BancoBrasil240Registro1


class ItauCnab400Registro0(CNAB400Registro0):
    _meta = {
        "tipo_registro": CNABField(
            length=1, default="0", validation=CNABFieldType.Int, required=True
        ),
        "operacao": CNABField(
            length=1, default="1", validation=CNABFieldType.Int, required=True
        ),
        "literal_remessa": CNABField(
            length=7, default="remessa", validation=CNABFieldType.Alfa, required=True
        ),
        "tipo_servico": CNABField(
            length=2, default="01", validation=CNABFieldType.Int, required=True
        ),
        "literal_servico": CNABField(
            length=15, default="COBRANCA", validation=CNABFieldType.Alfa, required=True
        ),
        "agencia": CNABField(
            length=4, default="", validation=CNABFieldType.Int, required=True
        ),
        "filler1": CNABField(
            length=2, default="0", validation=CNABFieldType.Int, required=True
        ),
        "conta": CNABField(
            length=5, default="", validation=CNABFieldType.Int, required=True
        ),
        "conta_dv": CNABField(
            length=1, default="", validation=CNABFieldType.Int, required=True
        ),
        "filler2": CNABField(
            length=8, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "nome_empresa": CNABField(
            length=30, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "codigo_banco": CNABField(
            length=3, default="341", validation=CNABFieldType.Int, required=True
        ),
        "nome_banco": CNABField(
            length=15,
            default="BANCO ITAU SA",
            validation=CNABFieldType.Alfa,
            required=True,
        ),
        "data_gravacao": CNABField(
            length=6,
            default="",  # nao informar a data na instanciação - gerada dinamicamente
            validation=CNABFieldType.Date,
            required=True,
        ),
        "filler3": CNABField(
            length=294, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "numero_sequencial": CNABField(
            length=6, default="1", validation=CNABFieldType.Int, required=True
        ),
    }

    def inserir_detalhe(self, **kwargs):
        from .registro1 import ItauCnab400Registro1
        return ItauCnab400Registro1(self, self, **kwargs)
