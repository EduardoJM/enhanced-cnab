from typing import Optional, Union
from cnab.base.cnab_400 import CNAB400Registro9
from cnab.core.field import CNABField, CNABFieldType
from cnab.utils.dict_utils import set_if_has_value
from cnab.base.registro import Registro


class ItauCnab400Registro9(CNAB400Registro9):
    _meta = {
        "tipo_registro": CNABField(
            length=1, default="9", validation=CNABFieldType.Int, required=True
        ),
        "filler1": CNABField(  # 32.3P
            length=393, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "numero_registro": CNABField(  # 4.3R
            length=6, default="0", validation=CNABFieldType.Int, required=True
        ),
    }
