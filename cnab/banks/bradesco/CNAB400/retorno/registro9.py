from cnab.base.retorno.CNAB400 import Registro9Retorno
from cnab.core.field import CNABFieldAlfa, CNABFieldDecimal, CNABFieldInteger


class BradescoRetornoCnab400Registro9(Registro9Retorno):
    tipo_registro = CNABFieldInteger("", length=1, default="9", required=True)
    ident_retorno = CNABFieldInteger("", length=1, default="2", required=True)
    ident__tipo_retorno = CNABFieldInteger("", length=2, default="01", required=True)
    codigo_banco = CNABFieldInteger("", length=3, default="237", required=True)
    filler0 = CNABFieldAlfa("", length=10, default="", required=True)
    qtd_titulos_cobranca = CNABFieldInteger("", length=8, default="1", required=True)
    valor_total_cobranca = CNABFieldDecimal(
        "",
        length=12,
        default="",
        precision=2,
        required=True,
    )
    n_aviso_bancario = CNABFieldAlfa("", length=8, default="1", required=True)
    filler1 = CNABFieldAlfa("", length=10, default=" ", required=True)
    QtdEntradaConfirmadaC02 = CNABFieldInteger("", length=5, default="", required=True)
    ValEntradaConfirmadaC02 = CNABFieldDecimal(
        "",
        length=10,
        default="",
        precision=2,
        required=True,
    )
    ValTotLiquidacaoC06 = CNABFieldDecimal(
        "",
        length=10,
        default="",
        precision=2,
        required=True,
    )
    QtdLiquidacaoC06 = CNABFieldInteger("", length=5, default="", required=True)
    ValLiquidacaoC06 = CNABFieldDecimal(
        "",
        length=10,
        default="",
        precision=2,
        required=True,
    )
    QtdBaixaC09C10 = CNABFieldInteger("", length=5, default="", required=True)
    ValBaixaC09C10 = CNABFieldDecimal(
        "",
        length=10,
        default="",
        precision=2,
        required=True,
    )
    QtdAbatimentoCanceladoC13 = CNABFieldInteger(
        "", length=5, default="", required=True
    )
    ValAbatimentoCanceladoC13 = CNABFieldDecimal(
        "",
        length=10,
        default="",
        precision=2,
        required=True,
    )
    QtdVencimentoAlteradoC14 = CNABFieldInteger("", length=5, default="", required=True)
    ValVencimentoAlteradoC14 = CNABFieldDecimal(
        "",
        length=10,
        default="",
        precision=2,
        required=True,
    )
    QtdAbatimentoConcedidoC12 = CNABFieldInteger(
        "", length=5, default="", required=True
    )
    ValAbatimentoConcedidoC12 = CNABFieldDecimal(
        "",
        length=10,
        default="",
        precision=2,
        required=True,
    )
    QtdConfirmacaoInstProtestoC19 = CNABFieldInteger(
        "", length=5, default="", required=True
    )
    ValConfirmacaoInstProtestoC19 = CNABFieldDecimal(
        "",
        length=10,
        default="",
        precision=2,
        required=True,
    )
    filler2 = CNABFieldAlfa("", length=174, default=" ", required=True)
    ValTotalRateiosEfetuados = CNABFieldDecimal(
        "",
        length=13,
        default="",
        precision=2,
        required=True,
    )
    QtdTotalRateiosEfetuados = CNABFieldInteger("", length=8, default="", required=True)
    filler3 = CNABFieldAlfa("", length=9, default=" ", required=True)
    numero_sequencial_registro = CNABFieldInteger(
        "", length=6, default="", required=True
    )
