from cnab.base.remessa.CNAB240 import CNAB240Registro3
from cnab.core.field import CNABFieldInteger, CNABFieldAlfa


class Caixa240Registro3S1e2(CNAB240Registro3):
    codigo_banco = CNABFieldInteger("",length=3, default="104", required=True)
    codigo_lote = CNABFieldInteger("",length=4, default=1, required=True)
    tipo_registro = CNABFieldInteger("",length=1, default="3", required=True)
    numero_registro = CNABFieldInteger("",length=5, default="0", required=True)
    seguimento = CNABFieldAlfa("",length=1, default="S", required=True)
    filler1 = CNABFieldAlfa("",length=1, default=" ", required=True)
    codigo_movimento = CNABFieldInteger("",length=2,default="01",required=True)
    tipo_impressao = CNABFieldInteger("",length=1, default="0", required=True)
    filler = CNABFieldInteger("",length=2, default="0", required=True)
    mensagem_140 = CNABFieldAlfa("",length=140, default=" ", required=True)
    filler2 = CNABFieldInteger("",length=2, default="0", required=True)
    filler3 = CNABFieldAlfa("",length=78, default=" ", required=True)
