from cnab.base.cnab_240 import CNAB240Registro3
from cnab.core.field import CNABField, CNABFieldType


class BancoBrasil240Registro3S3(CNAB240Registro3):
    _meta = {
        "codigo_banco": CNABField(  # 1.3S
            length=3, default="001", validation=CNABFieldType.Int, required=True
        ),
        "codigo_lote": CNABField(  # 2.3S
            length=4, default=1, validation=CNABFieldType.Int, required=True
        ),
        "tipo_registro": CNABField(  # 3.3S
            length=1, default="3", validation=CNABFieldType.Int, required=True
        ),
        "numero_registro": CNABField(  # 4.3S
            length=5, default="0", validation=CNABFieldType.Int, required=True
        ),
        "seguimento": CNABField(  # 5.3S
            length=1, default="S", validation=CNABFieldType.Alfa, required=True
        ),
        "filler1": CNABField(  # 6.3S
            length=1, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "codigo_movimento": CNABField(  # 7.3S
            length=2,
            default="01",  # entrada de titulo
            validation=CNABFieldType.Int,
            required=True,
        ),
        # - ------------------ até aqui é igual para todo registro tipo 3
        "tipo_impressao": CNABField(  # 8.3S
            length=1, default="0", validation=CNABFieldType.Int, required=True
        ),
        "mensagem_5": CNABField(  # 9.3S
            length=40, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "mensagem_6": CNABField(  # 10.3S
            length=40, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "mensagem_7": CNABField(  # 11.3S
            length=40, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "mensagem_8": CNABField(  # 12.3S
            length=40, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "filler2": CNABField(  # 13.3S
            length=40, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "filler3": CNABField(  # 14.3S
            length=22, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
    }
