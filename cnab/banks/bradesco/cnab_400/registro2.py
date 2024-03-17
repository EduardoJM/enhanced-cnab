from typing import Optional, Union
from cnab.base.cnab_400 import CNAB400Registro2
from cnab.core.field import CNABField, CNABFieldType
from cnab.utils.dict_utils import set_if_has_value
from cnab.base.registro import Registro


class BradescoCnab400Registro2(CNAB400Registro2):
    _meta = {
        "tipo_registro": CNABField(
            length=1, default="2", validation=CNABFieldType.Int, required=True
        ),
        "mensagem_1": CNABField(
            length=80, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "mensagem_2": CNABField(
            length=80, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "mensagem_3": CNABField(
            length=80, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "mensagem_4": CNABField(
            length=80, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "data_desconto": CNABField(
            length=6, default="0", validation=CNABFieldType.Date, required=True
        ),
        "vlr_desconto": CNABField(
            length=11,
            default="0",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "data_desconto_2": CNABField(
            length=6, default="0", validation=CNABFieldType.Date, required=True
        ),
        "vlr_desconto_2": CNABField(
            length=11,
            default="0",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "filler": CNABField(
            length=7, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "carteira_banco": CNABField(
            length=3, default="0", validation=CNABFieldType.Int, required=True
        ),
        "agencia": CNABField(
            length=5, default="0", validation=CNABFieldType.Int, required=True
        ),
        "conta": CNABField(
            length=7, default="0", validation=CNABFieldType.Int, required=True
        ),
        "conta_dv": CNABField(
            length=1, default="0", validation=CNABFieldType.Int, required=True
        ),
        "nosso_numero": CNABField(
            length=11, default="0", validation=CNABFieldType.Int, required=True
        ),
        "nosso_numero_dv": CNABField(
            length=1, default="0", validation=CNABFieldType.Alfa, required=True
        ),
        "numero_registro": CNABField(
            length=6, default="0", validation=CNABFieldType.Int, required=True
        ),
    }
