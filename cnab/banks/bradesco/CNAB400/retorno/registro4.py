from cnab.base.retorno.CNAB400 import Registro4Retorno
from cnab.core.field import CNABFieldInteger, CNABFieldAlfa

class BradescoRetornoCnab400Registro4(Registro4Retorno):
    tipo_registro = CNABFieldInteger("001-001",length=1,default='4',required=True)
    carteira = CNABFieldInteger("002-004",length=3,default='',required=True)
    agencia = CNABFieldInteger("005-009",length=5,default='',required=True)
    conta = CNABFieldInteger("010-016",length=7,default='',required=True)
    nosso_numero= CNABFieldInteger("017-027",length=11,default='',required=True)
    nosso_numero_dv= CNABFieldAlfa("028-028",length=1,default=' ',required=True)
    pix_url= CNABFieldAlfa("029-105",length=77,default=' ',required=True)
    txid= CNABFieldAlfa("106-140",length=35,default=' ',required=True)
    zero = CNABFieldAlfa("141-394",length=254,default=' ',required=True)
    numero_registro= CNABFieldInteger("395-400",length=6,default='0',required=True)
