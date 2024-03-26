from cnab.base.remessa.CNAB240 import CNAB240Registro5
from cnab.core.field import CNABFieldInteger, CNABFieldAlfa, CNABFieldDecimal


class Caixa240Registro5(CNAB240Registro5):
	codigo_banco = CNABFieldInteger("",length=3,default='104',required=True)
	codigo_lote = CNABFieldInteger("",length=4,default=1,required=True)
	tipo_registro = CNABFieldInteger("",length=1,default='5',required=True)
	filler1 = CNABFieldAlfa("",length=9,default=' ',required=True)
	qtd_registros = CNABFieldInteger("",length=6,default=' ',required=True)
	qtd_registros_cobranca_simples = CNABFieldInteger("",length=6,default='0',required=True)
	somatorio_valores_simples = CNABFieldDecimal("",length=15,default='0',precision=2,required=True)
	qtd_registros_cobranca_caucionadas = CNABFieldInteger("",length=6,default='0',required=True)
	somatorio_valores_caucionadas = CNABFieldDecimal("",length=15,default='0',precision=2,required=True)
	qtd_registros_cobranca_descontada = CNABFieldInteger("",length=6,default='0',required=True)
	somatorio_valores_descontada = CNABFieldDecimal("",length=15,default='0',precision=2,required=True)	
	filler2 = CNABFieldAlfa("",length=31,default=' ',required=True)
	filler3 = CNABFieldAlfa("",length=117,default=' ',required=True)
