from cnab.base.remessa.CNAB240 import CNAB240Registro9
from cnab.core.field import CNABFieldAlfa, CNABFieldInteger


class BancoBrasil240Registro9(CNAB240Registro9):
    codigo_banco = CNABFieldInteger("", length=3, default="001", required=True)
    codigo_lote = CNABFieldInteger("", length=4, default=9999, required=True)
    tipo_registro = CNABFieldInteger("", length=1, default="9", required=True)
    filler1 = CNABFieldAlfa("", length=9, default=" ", required=True)
    qtd_lotes = CNABFieldInteger("", length=6, default="1", required=True)
    qtd_registros = CNABFieldInteger("", length=6, default="0", required=True)
    filler2 = CNABFieldAlfa("", length=6, default=" ", required=True)
    filler3 = CNABFieldAlfa("", length=205, default=" ", required=True)
