from cnab.base.cnab_240 import CNAB240Registro1
from cnab.core.field import CNABFieldInteger, CNABFieldAlfa, CNABCreatedDateField
from .registro5 import Caixa240Registro5

class Caixa240Registro1(CNAB240Registro1):
	registro5_class = Caixa240Registro5
    
	codigo_banco = CNABFieldInteger("",length=3,default='104',required=True)
	codigo_lote = CNABFieldInteger("",length=4,default=1,required=True)
	tipo_registro = CNABFieldInteger("",length=1,default=1,required=True)
	operacao = CNABFieldAlfa("",length=1,default='R',required=True)
	tipo_servico = CNABFieldInteger("",length=2,default='01',required=True)
	filler1 = CNABFieldInteger("",length=2,default='0',required=True)
	versao_layout = CNABFieldInteger("",length=3,default='060',required=True)
	filler2 = CNABFieldAlfa("",length=1,default=' ',required=True)
	tipo_inscricao = CNABFieldInteger("",length=1,default='',required=True)
	numero_inscricao = CNABFieldInteger("",length=15,default='',required=True)
	codigo_beneficiario = CNABFieldInteger("",length=7, default="", required=True )
	filler3 = CNABFieldInteger("",length=13,default='0',required=True)
	agencia = CNABFieldInteger("",length=5,default='',required=True)
	agencia_dv = CNABFieldInteger("",length=1,default='',required=True)
	codigo_beneficiario_6 = CNABFieldInteger("",length=6, default="0", required=True )
	codigo_modelo_personalizado = CNABFieldInteger("",length=7, default="0", required=True,)
	filler4 = CNABFieldInteger("",length = 1,default = '0',required = True)
	nome_empresa = CNABFieldAlfa("",length=30,default='',required=True)
	mensagem_fixa1 = CNABFieldAlfa("",length=40,default=' ',required=True)
	mensagem_fixa2 = CNABFieldAlfa("",length=40,default=' ',required=True)
	numero_remessa = CNABFieldInteger("",length=8, default="0", required=True, value_from='numero_sequencial_arquivo')
	data_gravacao = CNABCreatedDateField("",length=8,required=True)
	filler5 = CNABFieldInteger("",length = 8,default = '0',required = True)
	filler6 = CNABFieldAlfa("",length = 33,default = ' ',required = True)

	def inserir_detalhe(self, **kwargs):
		from .registro3P import Caixa240Registro3P
		return Caixa240Registro3P(self.header, self, self, **kwargs)

	def get_versao_layout(self):
        # TODO: change this in future
		if self.versao_layout:
			return self.versao_layout

		if len(self.codigo_beneficiario) > 6:
			return '067'
		return '060'

	def get_codigo_beneficiario_6(self):
        # TODO: change this in future
		if self.codigo_beneficiario_6:
			return self.codigo_beneficiario_6
		if len(self.codigo_beneficiario) == 6:
			return self.codigo_beneficiario
		return "000000"

	def get_codigo_beneficiario(self):
        # TODO: change this in future
		versao_layout = self.get_versao_layout()
		if versao_layout == '060':
			code = str(self.codigo_beneficiario).rjust(6, '0')
			return f"{code}0"
		if versao_layout == '067':
			return str(self.codigo_beneficiario).rjust(7, '0')
		# TODO: raise exception here
