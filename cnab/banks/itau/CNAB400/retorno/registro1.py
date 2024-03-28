from cnab.base.retorno.CNAB400 import Registro1Retorno
from cnab.core.especie import CNABFieldEspecieTitulo
from cnab.core.field import (
    CNABFieldAlfa,
    CNABFieldDate,
    CNABFieldDecimal,
    CNABFieldInteger,
)


class ItauRetornoCnab400Registro1(Registro1Retorno):
    tipo_registro = CNABFieldInteger("001-001", length=1, default="1", required=True)
    tipo_inscricao_empresa = CNABFieldInteger(
        "002-003", length=2, default="", required=True
    )
    numero_inscricao_empresa = CNABFieldInteger(
        "004-017", length=14, default="", required=True
    )
    agencia = CNABFieldInteger("018-021", length=4, default="", required=True)
    filler1 = CNABFieldInteger("022-023", length=2, default="0", required=True)
    conta = CNABFieldInteger("024-028", length=5, default="", required=True)
    conta_dv = CNABFieldInteger("029-029", length=1, default="", required=True)
    filler2 = CNABFieldAlfa("030-037", length=8, default=" ", required=True)
    seu_numero = CNABFieldAlfa("038-062", length=25, default=" ", required=True)
    nosso_numero = CNABFieldInteger("063-070", length=8, default="", required=True)
    filler3 = CNABFieldAlfa("071-082", length=12, default=" ", required=True)
    carteira = CNABFieldInteger("083-085", length=3, default="0", required=True)
    filler34 = CNABFieldAlfa("086-094", length=9, default=" ", required=True)
    filler4 = CNABFieldAlfa("095-107", length=13, default=" ", required=True)
    cod_carteira = CNABFieldAlfa("108-108", length=1, default=" ", required=True)
    codigo_movimento = CNABFieldInteger(
        "109-110", length=2, default="01", required=True
    )
    data_ocorrencia = CNABFieldDate("111-116", length=6, default="0", required=True)
    seu_numero2 = CNABFieldAlfa("117-126", length=10, default="", required=True)
    filler41 = CNABFieldAlfa("127-134", length=8, default="", required=True)
    filler42 = CNABFieldAlfa("135-146", length=12, default="", required=True)
    data_vencimento = CNABFieldDate("147-152", length=6, default="", required=True)
    valor = CNABFieldDecimal(
        "153-165", length=11, default="", precision=2, required=True
    )
    codigo_banco = CNABFieldInteger("166-168", length=3, default="341", required=True)
    agencia_cobradora = CNABFieldInteger(
        "169-172", length=4, default="0", required=True
    )
    agencia_cobradora_dv = CNABFieldInteger(
        "173-173", length=1, default="0", required=True
    )
    especie_titulo = CNABFieldEspecieTitulo("174-175", length=2, required=True)
    vlr_tarifas = CNABFieldDecimal(
        "176-188", length=11, default="", precision=2, required=True
    )
    filler43 = CNABFieldAlfa("189-214", length=26, default="", required=True)
    vlr_iof = CNABFieldDecimal(
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
    boleto_dda = CNABFieldAlfa("293-293", length=1, default="", required=True)
    filler44 = CNABFieldAlfa("294-295", length=2, default=" ", required=True)
    data_credito = CNABFieldDate("296-301", length=6, default="", required=True)
    cod_instrucao_cancelada = CNABFieldAlfa(
        "302-305", length=4, default=" ", required=True
    )
    filler45 = CNABFieldAlfa("306-311", length=6, default=" ", required=True)
    filler46 = CNABFieldInteger("312-324", length=13, default="0", required=True)
    nome_pagador = CNABFieldAlfa("325-354", length=30, default="", required=True)
    filler47 = CNABFieldAlfa("355-377", length=23, default=" ", required=True)
    erros_mensagens = CNABFieldAlfa("378-385", length=8, default="", required=True)
    filler5 = CNABFieldAlfa("386-392", length=7, default="", required=True)
    cod_liquidacao = CNABFieldAlfa("393-394", length=2, default="", required=True)
    numero_registro = CNABFieldInteger("395-400", length=6, default="0", required=True)
