from cnab.base.remessa.CNAB400 import CNAB400Registro9
from cnab.core.field import CNABFieldInteger, CNABFieldAlfa


class ItauCnab400Registro9(CNAB400Registro9):
    tipo_registro = CNABFieldInteger("001-001", length=1, default="9", required=True)
    filler1 = CNABFieldAlfa("002-394", length=393, default=" ", required=True)
    numero_registro = CNABFieldInteger("395-400", length=6, default="0", required=True)
