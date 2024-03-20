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
			validation=CNABFieldType.Int,
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
    
    def inserir_detalhe(self, **kwargs):
        from .registro3P import Caixa240Registro3P
        return Caixa240Registro3P(self.header, self, self, **kwargs)

    def get_versao_layout(self):
        if self._data.get('versao_layout'):
            return self._data.get('versao_layout')

        codigo_beneficiario = self.get_data_or_parent('codigo_beneficiario')
        if len(codigo_beneficiario) > 6:
            return '067'
        return '060'
    
    def get_codigo_beneficiario_6(self):
        if self._data.get('codigo_beneficiario_6'):
            return self._data.get('codigo_beneficiario_6')
        codigo_beneficiario = self.get_data_or_parent('codigo_beneficiario')
        if len(codigo_beneficiario) == 6:
            return codigo_beneficiario
        return "000000"

    def get_codigo_beneficiario(self):
        codigo_beneficiario = self.get_data_or_parent('codigo_beneficiario')
        versao_layout = self.get_versao_layout()
        if versao_layout == '060':
            code = str(codigo_beneficiario).rjust(6, '0')
            return f"{code}0"
        if versao_layout == '067':
            return str(codigo_beneficiario).rjust(7, '0')
		# TODO: raise exception here
