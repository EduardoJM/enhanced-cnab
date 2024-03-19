from typing import Optional, Union, TYPE_CHECKING
from cnab.base.cnab_240 import CNAB240Registro1
from cnab.core.field import CNABField, CNABFieldType
from cnab.utils.dict_utils import set_if_has_value
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
			default='C', # C Compromisso de pagamento - D Compromisso de recebimento
			validation=CNABFieldType.Alfa,
			required=True),
		'tipo_servico_transf': CNABField(#05.1
			length=2,
			default='01',
			validation=CNABFieldType.Int,
			required=True),
		'forma_lancamento': CNABField(#06.1
			length=2,
			default='',
			validation=CNABFieldType.Int,
			required=True),
		'versa_layout': CNABField(#07.1
			length=3,
			default='041',
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
			length=14,
			default='',
			validation=CNABFieldType.Int,
			required=True),
		'convenio_caixa': CNABField(#11.1
			length=6,
			default='',
			validation=CNABFieldType.Int,
			required=True),
		'tipo_compromisso': CNABField(#11.1
			length=2,
			default='', #01 Pagamento a Fornecedor - 02 Pagamento de Salarios - 03 Autopagamento - 06 Salario Ampliacao de Base - 11 Debito em Conta			
			validation=CNABFieldType.Int,
			required=True),
		'codigo_compromisso': CNABField(#11.1
			length=4,
			default='0',
			validation=CNABFieldType.Int,
			required=True),
		'param_transmissao': CNABField(#11.1
			length=2,
			default='0',
			validation=CNABFieldType.Int,
			required=True),
		'filler3': CNABField(#11.1
			length=6,
			default=' ',
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
		'conta': CNABField(#14.1
			length = 12,
			default = '',
			validation = CNABFieldType.Int,
			required = True),
		'conta_dv': CNABField(#15.1
			length = 1,
			default = '',
			validation = CNABFieldType.Alfa,
			required = True),
		'filler4': CNABField(#16.1
			length = 1,
			default = ' ',
			validation = CNABFieldType.Alfa,
			required = True),
		'nome_empresa': CNABField(
			length=30,
			default='',
			validation=CNABFieldType.Alfa,
			required=True),
		'mensagem_fixa1': CNABField(# mensagems 1 e 2 : somente use para mensagens que serao impressas de forma identica em todos os boletos do lote
			length=40,
			default=' ',
			validation=CNABFieldType.Alfa,
			required=True),
		'logradouro' : CNABField(#19.1
			length = 30,
			default = '',
			validation = CNABFieldType.Alfa,
			required = True),
		'numero_endereco' : CNABField(#20.1
			length = 5,
			default = '',
			validation = CNABFieldType.Int,
			required = True),
		'complemento' : CNABField(#21.1
			length = 15,
			default = ' ',
			validation = CNABFieldType.Alfa,
			required = True),
		'cidade' : CNABField(#22.1
			length = 20,
			default = '',
			validation = CNABFieldType.Alfa,
			required = True),
		'cep': CNABField(#23.1
			length = 5,
			default = '',
			validation = CNABFieldType.Int,
			required = True),
		'complemento_cep': CNABField(#24.1
			length = 3,
			default = '',
			validation = CNABFieldType.Alfa,
			required = True),
		'estado' : CNABField(#25.1
			length = 2,
			default = '',
			validation = CNABFieldType.Alfa,
			required = True),
		'filler5' : CNABField(#26.1
			length = 8,
			default = ' ',
			validation = CNABFieldType.Alfa,
			required = True),
		'ocorrencias' : CNABField(#27.1
			length = 10,
			default = ' ',
			validation = CNABFieldType.Alfa,
			required = True),
    }
