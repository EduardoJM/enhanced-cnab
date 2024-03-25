from cnab.base.cnab_240 import CNAB240Registro5
from cnab.core.field import CNABFieldInteger, CNABFieldAlfa


class BancoBrasil240Registro5(CNAB240Registro5):
    codigo_banco = CNABFieldInteger("",length=3, default="001", required=True)
    codigo_lote = CNABFieldInteger("",length=4, default=1, required=True)
    tipo_registro = CNABFieldInteger("",length=1, default="5", required=True)
    filler1 = CNABFieldAlfa("",length=9, default=" ", required=True)
    qtd_registros = CNABFieldInteger("",length=6, default="0", required=True)
    filler3 = CNABFieldAlfa("",length=217, default=" ", required=True)
