from cnab.base.cnab_240 import CNAB240Registro5
from cnab.core.field import CNABField, CNABFieldType


class Caixa240Registro5(CNAB240Registro5):
    _meta = {
        'codigo_banco': CNABField(      #01.5
			length=3,
			default='104',
			validation=CNABFieldType.Int,
			required=True),
		'codigo_lote': CNABField(       #02.5
			length=4,
			default=1,
			validation=CNABFieldType.Int,
			required=True),
		'tipo_registro': CNABField(     #03.5
			length=1,
			default='5',
			validation=CNABFieldType.Int,
			required=True),
		'filler1': CNABField(          #04.5
			length=9,
			default=' ',
			validation=CNABFieldType.Alfa,
			required=True),
		'qtd_registros': CNABField(      #05.5
			length=6,
			default=' ',
			validation=CNABFieldType.Int,
			required=True),
        'qtd_registros_cobranca_simples': CNABField(      #06.5
			length=6,
			default='0',
			validation=CNABFieldType.Int,
			required=True),
		'somatorio_valores_simples': CNABField(# 07.5
			length=15,
			default='0',
			validation=CNABFieldType.Decimal,
			precision=2,
			required=True),
        'qtd_registros_cobranca_caucionadas': CNABField(      # 08.5
			length=6,
			default='0',
			validation=CNABFieldType.Int,
			required=True),
        'somatorio_valores_caucionadas': CNABField( # 09.5
			length=15,
			default='0',
			validation=CNABFieldType.Decimal,
			precision=2,
			required=True),
        'qtd_registros_cobranca_descontada': CNABField( # 10.5
			length=6,
			default='0',
			validation=CNABFieldType.Int,
			required=True),
        'somatorio_valores_descontada': CNABField( # 11.5
			length=15,
			default='0',
			validation=CNABFieldType.Decimal,
			precision=2,
			required=True),	
		'filler2': CNABField( # 12.5
			length=31,
			default=' ',
			validation=CNABFieldType.Alfa,
			required=True),
		'filler3': CNABField( # 13.5
			length=117,
			default=' ',
			validation=CNABFieldType.Alfa,
			required=True),
    }
