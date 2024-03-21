from cnab.base.retorno.CNAB400 import Registro4Retorno
from cnab.core.field import CNABField, CNABFieldType

class BradescoRetornoCnab400Registro4(Registro4Retorno):
    _meta = {
        'tipo_registro' : CNABField( # 001 a 001
            length=1,
            default='4',
            validation=CNABFieldType.Int,
            required=True),
        'carteira' : CNABField( # 002 a 004
            length=3,
            default='',
            validation=CNABFieldType.Int,
            required=True),
        'agencia' : CNABField( # 005 a 009
            length=5,
            default='',
            validation=CNABFieldType.Int,
            required=True),
        'conta' : CNABField( # 010 a 016 # Sem dígito
            length=7,
            default='',
            validation=CNABFieldType.Int,
            required=True),
        'nosso_numero' : CNABField( # 017 a 027
            length=11,
            default='',
            validation=CNABFieldType.Int,
            required=True),
        'nosso_numero_dv' : CNABField( # 028 a 028
            length=1,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'pix_url' : CNABField( # 029 a 105
            length=77,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'txid' : CNABField( # 106 a 140
            length=35,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'zero' : CNABField(#20.3
            length=254,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'numero_registro' : CNABField( # 395 a 400
            length=6,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
    }
