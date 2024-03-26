from cnab.base.remessa.CNAB240 import CNAB240Registro1
from cnab.core.field import (
    CNABFieldInteger,
    CNABFieldAlfa,
    CNABCreatedDateField,
)
from .registro5 import Santander240Registro5

class Santander240Registro1(CNAB240Registro1):
    registro5_class = Santander240Registro5
    
    codigo_banco = CNABFieldInteger("",length=3, default="033", required=True)
    codigo_lote = CNABFieldInteger("",length=4, default=1, required=True)
    tipo_registro = CNABFieldInteger("",length=1, default=1, required=True)
    operacao = CNABFieldAlfa("",length=1, default="R", required=True)
    tipo_servico = CNABFieldInteger("",length=2, default="01", required=True)
    filler1 = CNABFieldAlfa("",length=2, default=" ", required=True)
    versao_layout = CNABFieldInteger("",length=3, default="030", required=True)
    filler2 = CNABFieldAlfa("",length=1, default=" ", required=True)
    tipo_inscricao = CNABFieldInteger("",length=1, default="", required=True)
    numero_inscricao = CNABFieldInteger("",length=15, default="", required=True)
    filler3 = CNABFieldAlfa("",length=20, default=" ", required=True)
    agencia = CNABFieldInteger("",length=4, default="", required=True)
    filler12 = CNABFieldInteger("",length=4, default="0", required=True)
    codigo_beneficiario = CNABFieldInteger("",length=6, default="0", required=True)
    codigo_beneficiario_dv = CNABFieldInteger("",length=1, default="0", required=True)
    filler4 = CNABFieldAlfa("",length=5, default=" ", required=True)
    nome_empresa = CNABFieldAlfa("",length=30, default="", required=True)
    mensagem1 = CNABFieldAlfa("",length=40,default=" ",required=True,)
    mensagem2 = CNABFieldAlfa("",length=40,default=" ",required=True,)
    numero_remessa = CNABFieldInteger("",length=8, default="", required=True,value_from='numero_sequencial_arquivo')
    data_gravacao =  CNABCreatedDateField("",length=8,required=True,)
    filler5 = CNABFieldAlfa("",length=41, default=" ", required=True)


    def inserir_detalhe(self, **kwargs):
        from .registro3P import Santander240Registro3P
        return Santander240Registro3P(self.header, self, self, **kwargs)