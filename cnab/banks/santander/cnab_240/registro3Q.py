from cnab.base.cnab_240 import CNAB240Registro3
from cnab.core.field import CNABField, CNABFieldType

class Santander240Registro3Q(CNAB240Registro3):
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
            default='Q',
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
            default='01',
            validation=CNABFieldType.Int,
            required=True
        ),
        # - ------------------ até aqui é igual para todo registro tipo 3
        'tipo_inscricao': CNABField(
            length=1,
            default='',
            validation=CNABFieldType.Int,
            required=True
        ),
        'numero_inscricao': CNABField(
            length=15,
            default='',
            validation=CNABFieldType.Int,
            required=True
        ),
        'nome_pagador': CNABField(
            length=40,
            default='',
            validation=CNABFieldType.Alfa,
            required=True
        ),
        'endereco_pagador': CNABField(
            length=40,
            default='',
            validation=CNABFieldType.Alfa,
            required=True
        ),
        'bairro_pagador': CNABField(
            length=15,
            default='',
            validation=CNABFieldType.Alfa,
            required=True
        ),
        'cep_pagador': CNABField(
            length=8,
            default='',
            validation=CNABFieldType.Int,
            required=True
        ),
        'cidade_pagador': CNABField(
            length=15,
            default='',
            validation=CNABFieldType.Alfa,
            required=True
        ),
        'uf_pagador': CNABField(
            length=2,
            default='',
            validation=CNABFieldType.Alfa,
            required=True
        ),
        'tipo_incricao_avalista': CNABField(
            length=1,
            default='0',
            validation=CNABFieldType.Int,
            required=True
        ),
        'numero_incricao_avalista': CNABField(
            length=15,
            default='0',
            validation=CNABFieldType.Int,
            required=True
        ),
        'nome_avalista': CNABField(
            length=40,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True
        ),
        'identificador_carne': CNABField(
            length=3,
            default='0',
            validation=CNABFieldType.Int,
            required=True
        ),
        'sequencia_parcela': CNABField(
            length=3,
            default='0',
            validation=CNABFieldType.Int,
            required=True
        ),
        'total_parcela': CNABField(
            length=3,
            default='0',
            validation=CNABFieldType.Int,
            required=True
        ),
        'numero_plano': CNABField(
            length=3,
            default='0',
            validation=CNABFieldType.Int,
            required=True
        ),
        'filler13': CNABField(
            length=19,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True
        ),
    }
