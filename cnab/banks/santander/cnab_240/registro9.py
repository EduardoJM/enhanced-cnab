from cnab.base.cnab_240 import CNAB240Registro9
from cnab.core.field import CNABField, CNABFieldType

class Santander240Registro9(CNAB240Registro9):
    _meta = {
        'codigo_banco': CNABField(
            length=3,
            default='033',
            validation=CNABFieldType.Int,
            required=True
        ),
        'codigo_lote': CNABField(
            length=4,
            default=9999,
            validation=CNABFieldType.Int,
            required=True
        ),
        'tipo_registro': CNABField(
            length=1,
            default='9',
            validation=CNABFieldType.Int,
            required=True
        ),
        'filler1': CNABField(
            length=9,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True
        ),
        'qtd_lotes': CNABField(
            length=6,
            default='1',
            validation=CNABFieldType.Int,
            required=True
        ),
        'qtd_registros': CNABField(
            length=6,
            default='0',
            validation=CNABFieldType.Int,
            required=True
        ),
        'filler2': CNABField(
            length=211,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True
        ),
    }
