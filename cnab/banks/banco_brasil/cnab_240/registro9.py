from cnab.base.cnab_240 import CNAB240Registro9
from cnab.core.field import CNABField, CNABFieldType


class BancoBrasil240Registro9(CNAB240Registro9):
    _meta = {
        "codigo_banco": CNABField(  # 01.5
            length=3, default="001", validation=CNABFieldType.Int, required=True
        ),
        "codigo_lote": CNABField(  # 02.5
            length=4, default=9999, validation=CNABFieldType.Int, required=True
        ),
        "tipo_registro": CNABField(  # 03.5
            length=1, default="9", validation=CNABFieldType.Int, required=True
        ),
        "filler1": CNABField(  # 04.5
            length=9, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "qtd_lotes": CNABField(  # 05.5
            length=6, default="1", validation=CNABFieldType.Int, required=True
        ),
        "qtd_registros": CNABField(  # 06.5
            length=6, default="0", validation=CNABFieldType.Int, required=True
        ),
        "filler2": CNABField(  # 12.5
            length=6, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "filler3": CNABField(  # 13.5
            length=205, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
    }
