from cnab.base.cnab_240 import CNAB240Registro3
from cnab.core.field import CNABField, CNABFieldType


class Caixa240Registro3R(CNAB240Registro3):
    _meta = {
        "codigo_banco": CNABField(  # 1.3R
            length=3, default="104", validation=CNABFieldType.Int, required=True
        ),
        "codigo_lote": CNABField(  # 2.3R
            length=4, default=1, validation=CNABFieldType.Int, required=True
        ),
        "tipo_registro": CNABField(  # 3.3R
            length=1, default="3", validation=CNABFieldType.Int, required=True
        ),
        "numero_registro": CNABField(  # 4.3R
            length=5, default="0", validation=CNABFieldType.Int, required=True
        ),
        "seguimento": CNABField(  # 5.3R
            length=1, default="R", validation=CNABFieldType.Alfa, required=True
        ),
        "filler1": CNABField(  # 6.3R
            length=1, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "codigo_movimento": CNABField(  # 7.3R
            length=2,
            default="01",  # entrada de titulo
            validation=CNABFieldType.Int,
            required=True,
        ),
        # - ------------------ até aqui é igual para todo registro tipo 3
        "codigo_desconto2": CNABField(  # 8.3R
            length=1, default="0", validation=CNABFieldType.Int, required=True
        ),
        "data_desconto2": CNABField(  # 9.3R
            length=8, default="0", validation=CNABFieldType.Date, required=True
        ),
        "vlr_desconto2": CNABField(  # 10.3R
            length=13,
            default="0",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "codigo_desconto3": CNABField(  # 11.3R
            length=1, default="0", validation=CNABFieldType.Int, required=True
        ),
        "data_desconto3": CNABField(  # 12.3R
            length=8, default="0", validation=CNABFieldType.Date, required=True
        ),
        "vlr_desconto3": CNABField(  # 13.3R
            length=13,
            default="0",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "codigo_multa": CNABField(  # 14.3R
            length=1, default="0", validation=CNABFieldType.Int, required=True
        ),
        "data_multa": CNABField(  # 15.3R
            length=8, default="0", validation=CNABFieldType.Date, required=True
        ),
        "vlr_multa": CNABField(  # 16.3R
            length=13,
            default="0",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "informacao_pagador": CNABField(  # 17.3R
            length=10, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "mensagem_3": CNABField(  # 18.3
            length=40, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "mensagem_4": CNABField(  # 19.3R
            length=40, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "filler2": CNABField(  # 20.3R
            length=50, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "filler3": CNABField(  # 20.3R
            length=11, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
    }
