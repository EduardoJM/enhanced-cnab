from cnab.base.cnab_240 import CNAB240Registro1
from cnab.core.field import CNABCreatedDateField, CNABField, CNABFieldType
from .registro5 import Caixa240Registro5

class Caixa240Registro1(CNAB240Registro1):
    registro5_class = Caixa240Registro5
    _meta = {
        'codigo_banco': CNABField(#01.1
			length=3,
			default='104',
			validation=CNABFieldType.Int,
			required=True),
		'codigo_lote': CNABField(#02.1
			length=4,
			default=1,
			validation=CNABFieldType.Int,
			required=True),
		'tipo_registro': CNABField(#3.1
			length=1,
			default=1,
			validation=CNABFieldType.Int,
			required=True),
		'operacao': CNABField(#04.1
			length=1,
			default='R',
			validation=CNABFieldType.Alfa,
			required=True),
		'tipo_servico': CNABField(#05.1
			length=2,
			default='01',
			validation=CNABFieldType.Int,
			required=True),
		'filler1': CNABField(#06.1
			length=2,
			default='0',
			validation=CNABFieldType.Int,
			required=True),
		'versao_layout': CNABField(#07.1
            # TODO: lidar com diferentes layouts
			length=3,
			default='060',
			validation=CNABFieldType.Int,
			required=True),
		'filler2': CNABField(#08.1
			length=1,
			default=' ',
			validation=CNABFieldType.Alfa,
			required=True),
		'tipo_inscricao': CNABField(#09.1
			length=1,
			default='',
			validation=CNABFieldType.Int,
			required=True),
		'numero_inscricao': CNABField(#10.1
			length=15,
			default='',
			validation=CNABFieldType.Int,
			required=True),
        "codigo_beneficiario": CNABField( # 11.1
            # TODO: lidar com diferentes layouts
            length=7, default="", validation=CNABFieldType.Int, required=True 
        ),
        'filler3': CNABField( # 11.1A
			length=13,
			default='0',
			validation=CNABFieldType.Alfa,
			required=True),
		'agencia': CNABField(#12.1
			length=5,
			default='',
			validation=CNABFieldType.Int,
			required=True),
		'agencia_dv': CNABField(#13.1
			length=1,
			default='',
			validation=CNABFieldType.Int,
			required=True),
        "codigo_beneficiario_6": CNABField( # 14.1
            # TODO: lidar com diferentes layouts
            length=6, default="0", validation=CNABFieldType.Int, required=True 
        ),
        "codigo_modelo_personalizado": CNABField(
            length=7, default="0", validation=CNABFieldType.Int, required=True,
		),
		'filler4': CNABField(#16.1
			length = 1,
			default = '0',
			validation = CNABFieldType.Int,
			required = True),
		'nome_empresa': CNABField( #17.1
			length=30,
			default='',
			validation=CNABFieldType.Alfa,
			required=True),
		'mensagem_fixa1': CNABField( # 18.1
            # mensagems 1 e 2 : somente use para mensagens que serao impressas de forma identica em todos os boletos do lote
			length=40,
			default=' ',
			validation=CNABFieldType.Alfa,
			required=True),
		'mensagem_fixa2': CNABField( # 19.1
            # mensagems 1 e 2 : somente use para mensagens que serao impressas de forma identica em todos os boletos do lote
			length=40,
			default=' ',
			validation=CNABFieldType.Alfa,
			required=True),
        "numero_remessa": CNABField(  # 20.1
            length=8, default="0", validation=CNABFieldType.Int, required=True
        ),
        "data_gravacao": CNABCreatedDateField(  # 21.1
            length=8,
            validation=CNABFieldType.Date,
            required=True,
        ),
		'filler5' : CNABField( # 22.1
			length = 8,
			default = '0',
			validation = CNABFieldType.Int,
			required = True),
		'filler6' : CNABField( # 23.1
			length = 33,
			default = ' ',
			validation = CNABFieldType.Alfa,
			required = True),
    }
