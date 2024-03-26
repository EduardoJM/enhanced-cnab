from cnab.base.remessa.CNAB240 import CNAB240Registro0
from cnab.core.field import (
    CNABFieldInteger,
    CNABFieldAlfa,
    CNABCreatedDateField,
)
from .registro1 import Santander240Registro1

class Santander240Registro0(CNAB240Registro0):
    registro1_class = Santander240Registro1
    
    codigo_banco = CNABFieldInteger("",length=3,default="033",required=True,)
    codigo_lote = CNABFieldInteger("",length=4,default="0000",required=True,)
    tipo_registro = CNABFieldInteger("",length=1,default="0",required=True,)
    filler1 = CNABFieldAlfa("",length=8,default=" ",required=True,)
    tipo_inscricao = CNABFieldInteger("",length=1,default="",required=True,)
    numero_inscricao = CNABFieldInteger("",length=15,default="",required=True,)
    agencia = CNABFieldInteger("",length=4,default="",required=True,)
    filler12 = CNABFieldInteger("",length=4,default="0",required=True,)
    codigo_beneficiario = CNABFieldInteger("",length=6,default="0",required=True,)
    codigo_beneficiario_dv = CNABFieldInteger("",length=1,default="0",required=True,)
    filler2 = CNABFieldAlfa("",length=25,default=" ",required=True,)
    nome_empresa = CNABFieldAlfa("",length=30,default="",required=True,)
    nome_banco = CNABFieldAlfa("",length=30,default="BANCO SANTANDER",required=True,)
    filler3 = CNABFieldAlfa("",length=10,default=" ",required=True,)
    codigo_remessa = CNABFieldInteger("",length=1,default="1",required=True,)
    data_geracao =  CNABCreatedDateField("",length=8,required=True,)
    filler4 = CNABFieldAlfa("",length=6,default=" ",required=True,)
    numero_sequencial_arquivo = CNABFieldInteger("",length=6,default="",required=True,)
    versao_layout = CNABFieldInteger("",length=3,default="040",required=True,)
    filler5 = CNABFieldAlfa("",length=74,default=" ",required=True,)

