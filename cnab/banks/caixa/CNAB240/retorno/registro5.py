from cnab.base.retorno.CNAB240 import Registro5Retorno
from cnab.core.field import CNABFieldAlfa, CNABFieldDecimal, CNABFieldInteger


class CaixaRetornoCnab240Registro5(Registro5Retorno):
    codigo_banco = CNABFieldInteger("", length=3, default="104", required=True)
    codigo_lote = CNABFieldInteger("", length=4, default=1, required=True)
    tipo_registro = CNABFieldInteger("", length=1, default="5", required=True)
    filler1 = CNABFieldAlfa("", length=1, default=" ", required=True)
    qtd_registros = CNABFieldInteger("", length=9, default=" ", required=True)
    qtd_titulos_simples = CNABFieldInteger("", length=6, default="0", required=True)
    vrl_titulos_simples = CNABFieldDecimal(
        "", length=15, default="0", precision=2, required=True
    )
    qtd_titulos_caucionada = CNABFieldInteger("", length=6, default="0", required=True)
    vlr_titulos_caucionada = CNABFieldDecimal(
        "", length=15, default="0", precision=2, required=True
    )
    qtd_titulos_descontada = CNABFieldInteger("", length=6, default="0", required=True)
    vlr_titulos_descontada = CNABFieldDecimal(
        "", length=15, default="0", precision=2, required=True
    )
    filler2 = CNABFieldAlfa("", length=31, default=" ", required=True)
    filler3 = CNABFieldAlfa("", length=117, default=" ", required=True)
