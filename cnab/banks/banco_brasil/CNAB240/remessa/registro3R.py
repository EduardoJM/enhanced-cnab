from cnab.base.remessa.CNAB240 import CNAB240Registro3
from cnab.core.field import (
    CNABFieldInteger,
    CNABFieldAlfa,
    CNABFieldDate,
    CNABFieldDecimal,
)


class BancoBrasil240Registro3R(CNAB240Registro3):
    codigo_banco = CNABFieldInteger("", length=3, default="001", required=True)
    codigo_lote = CNABFieldInteger("", length=4, default=1, required=True)
    tipo_registro = CNABFieldInteger("", length=1, default="3", required=True)
    numero_registro = CNABFieldInteger("", length=5, default="0", required=True)
    seguimento = CNABFieldAlfa("", length=1, default="R", required=True)
    filler1 = CNABFieldAlfa("", length=1, default=" ", required=True)
    codigo_movimento = CNABFieldInteger("", length=2, default="01", required=True)
    codigo_desconto2 = CNABFieldInteger("", length=1, default="0", required=True)
    data_desconto2 = CNABFieldDate("", length=8, default="0", required=True)
    vlr_desconto2 = CNABFieldDecimal(
        "", length=13, default="0", precision=2, required=True
    )
    codigo_desconto3 = CNABFieldInteger("", length=1, default="0", required=True)
    data_desconto3 = CNABFieldDate("", length=8, default="0", required=True)
    vlr_desconto3 = CNABFieldDecimal(
        "", length=13, default="0", precision=2, required=True
    )
    codigo_multa = CNABFieldInteger("", length=1, default="0", required=True)
    data_multa = CNABFieldDate("", length=8, default="0", required=True)
    vlr_multa = CNABFieldDecimal("", length=13, default="0", precision=2, required=True)
    informacao_pagador = CNABFieldAlfa("", length=10, default=" ", required=True)
    mensagem_3 = CNABFieldAlfa("", length=40, default=" ", required=True)
    mensagem_4 = CNABFieldAlfa("", length=40, default=" ", required=True)
    filler2 = CNABFieldAlfa("", length=20, default=" ", required=True)
    ocor_pagador = CNABFieldInteger("", length=8, default="0", required=True)
    cod_banco = CNABFieldInteger("", length=3, default="0", required=True)
    cod_agencia = CNABFieldInteger("", length=5, default="0", required=True)
    verificador_agencia = CNABFieldAlfa("", length=1, default="0", required=True)
    conta_corrente = CNABFieldInteger("", length=12, default="0", required=True)
    dv_conta = CNABFieldAlfa("", length=1, default="0", required=True)
    dv_ag = CNABFieldAlfa("", length=1, default="0", required=True)
    aviso_debito = CNABFieldInteger("", length=1, default="0", required=True)
    filler3 = CNABFieldAlfa("", length=9, default=" ", required=True)
