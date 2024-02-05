from cnab.base.cnab_240 import CNAB240Registro5
from cnab.core.field import CNABField, CNABFieldType


class BancoBrasil240Registro5(CNAB240Registro5):
    _meta = {
        "codigo_banco": CNABField(  # 01.5
            length=3, default="001", validation=CNABFieldType.Int, required=True
        ),
        "codigo_lote": CNABField(  # 02.5
            length=4, default=1, validation=CNABFieldType.Int, required=True
        ),
        "tipo_registro": CNABField(  # 03.5
            length=1, default="5", validation=CNABFieldType.Int, required=True
        ),
        "filler1": CNABField(  # 04.5
            length=9, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "qtd_registros": CNABField(  # 05.5
            length=6, default="0", validation=CNABFieldType.Int, required=True
        ),
        "filler3": CNABField(  # 13.5
            length=217, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
    }
