from cnab.base.remessa.CNAB400 import CNAB400Registro2
from cnab.core.field import CNABFieldAlfa, CNABFieldInteger, CNABFieldDate, CNABFieldDecimal


class ItauCnab400Registro2(CNAB400Registro2):
    tipo_registro = CNABFieldInteger("001-001", length=1, default="2", required=True)
    codigo_multa = CNABFieldAlfa("002-002", length=1, default="1", required=True)
    data_multa = CNABFieldDate("003-010", length=8, default="0", required=True)
    vlr_multa = CNABFieldDecimal("011-023", length=11,default="0",precision=2, required=True)
    filler2 = CNABFieldAlfa("024-394", length=371, default=" ", required=True)
    numero_registro = CNABFieldInteger("395-400", length=6, default="0", required=True)
