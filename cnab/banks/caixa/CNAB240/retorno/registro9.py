from cnab.base.retorno.CNAB240 import Registro9Retorno
from cnab.core.field import CNABFieldAlfa, CNABFieldInteger


class CaixaRetornoCnab240Registro9(Registro9Retorno):
    codigo_banco = CNABFieldInteger("", length=3, default="104", required=True)
    codigo_lote = CNABFieldInteger("", length=4, default=9999, required=True)
    tipo_registro = CNABFieldInteger("", length=1, default="9", required=True)
    filler1 = CNABFieldAlfa("", length=9, default=" ", required=True)
    qtd_lotes = CNABFieldInteger("", length=6, default="1", required=True)
    qtd_registros = CNABFieldInteger("", length=6, default="0", required=True)
    filler2 = CNABFieldAlfa("", length=6, default=" ", required=True)
    filler3 = CNABFieldInteger("", length=105, default=" ", required=True)
