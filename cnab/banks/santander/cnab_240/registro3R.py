from cnab.base.cnab_240 import CNAB240Registro3
from cnab.core.field import CNABField, CNABFieldType

class Santander240Registro3R(CNAB240Registro3):
    _meta = {
        'codigo_banco': CNABField(
            length=3,
            default='033',
            validation=CNABFieldType.Int,
            required=True
        ),
        'codigo_lote': CNABField(
            length=4,
            default=1,
            validation=CNABFieldType.Int,
            required=True
        ),
        'tipo_registro': CNABField(
            length=1,
            default='3',
            validation=CNABFieldType.Int,
            required=True
        ),
        'numero_registro': CNABField(
            length=5,
            default='0',
            validation=CNABFieldType.Int,
            required=True
        ),
        'seguimento': CNABField(
            length=1,
            default='R',
            validation=CNABFieldType.Alfa,
            required=True
        ),
        'filler1': CNABField(
            length=1,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True
        ),
        'codigo_movimento': CNABField(
            length=2,
            default='01', # entrada de titulo
            validation=CNABFieldType.Int,
            required=True
        ),
        # - ------------------ ate aqui é igual para todo registro tipo 3
        'codigo_desconto2': CNABField(
            length=1,
            default='0',
            validation=CNABFieldType.Int,
            required=True
        ),
        'data_desconto2': CNABField(
            length=8,
            default='0',
            validation=CNABFieldType.Date,
            required=True
        ),
        'vlr_desconto2': CNABField(
            length=13,
            default='0',
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True
        ),
        'filler14': CNABField(
            length=24,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True
        ),
        'codigo_multa': CNABField(
            length=1,
            default='1',
            validation=CNABFieldType.Int,
            required=True
        ),
        'data_multa': CNABField(
            length=8,
            default='0',
            validation=CNABFieldType.Date,
            required=True
        ),
        'vlr_multa': CNABField(
            length=13,
            default='0',
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True
        ),
        'filler15': CNABField(
            length=10,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True
        ),
        'mensagem3': CNABField(
            length=40,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True
        ),
        'mensagem4': CNABField(
            length=40,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True
        ),
        'filler16': CNABField(
            length=61,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True
        ),
    }
