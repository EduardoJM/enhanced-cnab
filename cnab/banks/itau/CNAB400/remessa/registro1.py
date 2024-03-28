from typing import Optional
from cnab.base.remessa.CNAB400 import CNAB400Registro1
from cnab.core.field import (
    CNABFieldInteger,
    CNABFieldAlfa,
    CNABFieldDecimal,
    CNABFieldDate,
)
from cnab.core.especie import CNABFieldEspecieTitulo
from cnab.base.remessa import RegistroRemessa
from .registro2 import ItauCnab400Registro2


class ItauCnab400Registro1(CNAB400Registro1):
    tipo_registro = CNABFieldInteger("", length=1, default="1", required=True)
    tipo_inscricao_empresa = CNABFieldInteger("", length=2, default="", required=True)
    numero_inscricao_empresa = CNABFieldInteger(
        "", length=14, default="", required=True
    )
    agencia = CNABFieldInteger("", length=4, default="", required=True)
    filler1 = CNABFieldInteger("", length=2, default="0", required=True)
    conta = CNABFieldInteger("", length=5, default="", required=True)
    conta_dv = CNABFieldInteger("", length=1, default="", required=True)
    filler2 = CNABFieldAlfa("", length=4, default=" ", required=True)
    cod_intrucao = CNABFieldInteger("", length=4, default="0", required=True)
    seu_numero = CNABFieldAlfa("", length=25, default=" ", required=True)
    nosso_numero = CNABFieldInteger("", length=8, default="", required=True)
    qtd_moeda = CNABFieldDecimal("", length=8, default="0", precision=5, required=True)
    carteira_banco = CNABFieldInteger("", length=3, default="0", required=True)
    filler3 = CNABFieldAlfa("", length=21, default=" ", required=True)
    cod_carteira = CNABFieldAlfa("", length=1, default=" ", required=True)
    codigo_movimento = CNABFieldInteger(
        "",
        length=2,
        default="01",
        required=True,
    )
    numero_documento = CNABFieldAlfa("", length=10, default=" ", required=True)
    data_vencimento = CNABFieldDate("", length=6, default="", required=True)
    valor = CNABFieldDecimal("", length=11, default="", precision=2, required=True)
    codigo_banco = CNABFieldInteger("", length=3, default="341", required=True)
    agencia_cobradora = CNABFieldInteger("", length=5, default="0", required=True)
    especie_titulo = CNABFieldEspecieTitulo("", length=2, required=True)
    aceite = CNABFieldAlfa("", length=1, default="N", required=True)
    data_emissao = CNABFieldDate("", length=6, default="", required=True)
    cod_instrucao1 = CNABFieldAlfa("", length=2, default=" ", required=True)
    cod_instrucao2 = CNABFieldAlfa("", length=2, default=" ", required=True)
    vlr_juros = CNABFieldDecimal("", length=11, default="0", precision=2, required=True)
    data_desconto = CNABFieldDate("", length=6, default="0", required=True)
    vlr_desconto = CNABFieldDecimal(
        "", length=11, default="0", precision=2, required=True
    )
    vlr_IOF = CNABFieldDecimal("", length=11, default="0", precision=2, required=True)
    vlr_abatimento = CNABFieldDecimal(
        "", length=11, default="0", precision=2, required=True
    )
    tipo_inscricao = CNABFieldInteger("", length=2, default="", required=True)
    numero_inscricao = CNABFieldInteger("", length=14, default="", required=True)
    nome_pagador = CNABFieldAlfa("", length=30, default="", required=True)
    filler4 = CNABFieldAlfa("", length=10, default=" ", required=True)
    endereco_pagador = CNABFieldAlfa("", length=40, default="", required=True)
    bairro_pagador = CNABFieldAlfa("", length=12, default="", required=True)
    cep_pagador = CNABFieldInteger("", length=8, default="", required=True)
    cidade_pagador = CNABFieldAlfa("", length=15, default="", required=True)
    uf_pagador = CNABFieldAlfa("", length=2, default="", required=True)
    nome_avalista = CNABFieldAlfa("", length=30, default=" ", required=True)
    filler5 = CNABFieldAlfa("", length=4, default=" ", required=True)
    data_mora = CNABFieldDate("", length=6, default="0", required=True)
    prazo_baixa = CNABFieldInteger("", length=2, default="0", required=True)
    filler6 = CNABFieldAlfa("", length=1, default=" ", required=True)
    numero_registro = CNABFieldInteger("", length=6, default="0", required=True)

    def __init__(
        self,
        header: Optional[RegistroRemessa],
        parent: Optional[RegistroRemessa],
        **kwargs: dict,
    ):
        super().__init__(header, parent, **kwargs)
        self.inserir_multa(**kwargs)

    def inserir_multa(self, **kwargs: dict):
        if not kwargs.get("data_multa"):
            return
        ItauCnab400Registro2(self.header, self, **kwargs)
