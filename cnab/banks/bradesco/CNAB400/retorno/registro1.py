from cnab.base.retorno.CNAB400 import Registro1Retorno
from cnab.core.field import (
    CNABFieldInteger,
    CNABFieldAlfa,
    CNABFieldDate,
    CNABFieldDecimal,
)
from cnab.core.especie import CNABFieldEspecieTitulo


class BradescoRetornoCnab400Registro1(Registro1Retorno):
    tipo_registro = CNABFieldInteger("001-001", length=1, default="1", required=True)
    tipo_inscricao_empresa = CNABFieldInteger(
        "002-003", length=2, default="", required=True
    )
    numero_inscricao_empresa = CNABFieldAlfa(
        "004-017", length=14, default="", required=True
    )
    filler1 = CNABFieldInteger("018-020", length=3, default="0", required=True)
    zero = CNABFieldInteger("021-021", length=1, default="0", required=True)
    carteira = CNABFieldInteger("022-024", length=3, default="", required=True)
    agencia = CNABFieldAlfa("025-029", length=5, default="", required=True)
    conta = CNABFieldAlfa("030-036", length=7, default="", required=True)
    conta_dv = CNABFieldAlfa("037-037", length=1, default="", required=True)
    seu_numero = CNABFieldAlfa("038-062", length=25, default=" ", required=True)
    filler2 = CNABFieldAlfa("063-070", length=8, default=" ", required=True)
    nosso_numero = CNABFieldInteger("071-081", length=11, default="", required=True)
    nosso_numero_dv = CNABFieldAlfa("082-082", length=1, default=" ", required=True)
    filler3 = CNABFieldAlfa("083-092", length=10, default=" ", required=True)
    filler4 = CNABFieldAlfa("093-104", length=12, default=" ", required=True)
    rateio_credito = CNABFieldAlfa("105-105", length=1, default="", required=True)
    filler41 = CNABFieldAlfa("106-107", length=2, default=" ", required=True)
    cod_carteira = CNABFieldAlfa("108-108", length=1, default=" ", required=True)
    codigo_movimento = CNABFieldAlfa("109-110", length=2, default="01", required=True)
    data_ocorrencia = CNABFieldDate("111-116", length=6, default="", required=True)
    seu_numero2 = CNABFieldAlfa("117-126", length=10, default="", required=True)
    nosso_numero2 = CNABFieldAlfa("127-146", length=20, default="", required=True)
    data_vencimento = CNABFieldDate("147-152", length=6, default="", required=True)
    valor = CNABFieldDecimal(
        "153-165", length=11, default="", precision=2, required=True
    )
    codigo_banco = CNABFieldInteger("166-168", length=3, default="237", required=True)
    agencia_cobradora = CNABFieldAlfa("169-173", length=5, default="0", required=True)
    especie_titulo = CNABFieldEspecieTitulo("174-175", length=2, required=True)
    vlr_despesas_cobranca = CNABFieldDecimal(
        "176-188", length=11, default="", precision=2, required=True
    )
    vlr_outras_despesas = CNABFieldDecimal(
        "189-201", length=11, default="", precision=2, required=True
    )
    vlr_juros_atraso = CNABFieldDecimal(
        "202-214", length=11, default="", precision=2, required=True
    )
    vlr_iof_devido = CNABFieldDecimal(
        "215-227", length=11, default="", precision=2, required=True
    )
    vlr_abatimento = CNABFieldDecimal(
        "228-240", length=11, default="", precision=2, required=True
    )
    vlr_desconto = CNABFieldDecimal(
        "241-253", length=11, default="", precision=2, required=True
    )
    vlr_pago = CNABFieldDecimal(
        "254-266", length=11, default="", precision=2, required=True
    )
    vlr_juros_multa = CNABFieldDecimal(
        "267-279", length=11, default="", precision=2, required=True
    )
    vlr_outros = CNABFieldDecimal(
        "280-292", length=11, default="", precision=2, required=True
    )
    filler44 = CNABFieldAlfa("293-294", length=2, default=" ", required=True)
    motivo25 = CNABFieldAlfa("295-295", length=1, default=" ", required=True)
    data_credito = CNABFieldDate("296-301", length=6, default="", required=True)
    origem_pagto = CNABFieldAlfa("302-304", length=3, default=" ", required=True)
    filler45 = CNABFieldAlfa("305-314", length=10, default=" ", required=True)
    codigo_banco_cheque = CNABFieldInteger(
        "315-318", length=4, default="0", required=True
    )
    motivo_rejeicao = CNABFieldAlfa("319-328", length=10, default="", required=True)
    filler47 = CNABFieldAlfa("329-368", length=40, default=" ", required=True)
    codigo_cartorio = CNABFieldAlfa("369-370", length=2, default="", required=True)
    numero_protocolo = CNABFieldAlfa("371-380", length=10, default="", required=True)
    filler5 = CNABFieldAlfa("381-394", length=14, default="", required=True)
    numero_registro = CNABFieldInteger("395-400", length=6, default="0", required=True)
