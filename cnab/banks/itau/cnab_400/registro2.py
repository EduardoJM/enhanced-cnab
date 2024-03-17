from cnab.base.cnab_400 import CNAB400Registro2
from cnab.core.field import CNABField, CNABFieldType


class ItauCnab400Registro2(CNAB400Registro2):
    _meta = {
        "tipo_registro": CNABField(
            length=1, default="2", validation=CNABFieldType.Int, required=True
        ),
        "codigo_multa": CNABField(  # 24.3P
            length=1, default="1", validation=CNABFieldType.Alfa, required=True
        ),
        "data_multa": CNABField(  # 31.3P
            length=8, default="0", validation=CNABFieldType.Date, required=True
        ),
        "vlr_multa": CNABField(  # 29.3P
            length=13,
            default="0",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "filler2": CNABField(  # 32.3P
            length=371, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "numero_registro": CNABField(  # 4.3R
            length=6, default="0", validation=CNABFieldType.Int, required=True
        ),
    }
