from typing import List, Union
from cnab.base.retorno.CNAB240 import Registro3Retorno
from cnab.core.field import (
    CNABFieldInteger,
    CNABFieldAlfa,
    CNABFieldDate,
    CNABFieldDecimal,
)
from .registro3U import CaixaRetornoCnab240Registro3U
from .registro3Y08 import CaixaRetornoCnab240Registro3Y08


class CaixaRetornoCnab240Registro3T(Registro3Retorno):
    children: List[
        Union[CaixaRetornoCnab240Registro3U, CaixaRetornoCnab240Registro3Y08]
    ] = []

    codigo_banco = CNABFieldInteger("", length=3, default="104", required=True)
    codigo_lote = CNABFieldInteger("", length=4, default=1, required=True)
    tipo_registro = CNABFieldInteger("", length=1, default="3", required=True)
    numero_registro = CNABFieldInteger("", length=5, default="0", required=True)
    seguimento = CNABFieldAlfa("", length=1, default="T", required=True)
    filler1 = CNABFieldAlfa("", length=1, default=" ", required=True)
    codigo_movimento = CNABFieldInteger("", length=2, default="01", required=True)
    agencia = CNABFieldInteger("", length=5, default="", required=True)
    agencia_dv = CNABFieldAlfa("", length=1, default="", required=True)
    codigo_convenio = CNABFieldInteger("", length=7, default="0", required=True)
    filler2 = CNABFieldInteger("", length=2, default="0", required=True)
    num_banco_pagadores = CNABFieldInteger("", length=3, default="0", required=True)
    filler3 = CNABFieldInteger("", length=1, default="0", required=True)
    filler4 = CNABFieldAlfa("", length=3, default=" ", required=True)
    carteira = CNABFieldInteger("", length=2, default="0", required=True)
    nosso_numero = CNABFieldInteger("", length=15, default="", required=True)
    dv_nosso_numero = CNABFieldInteger("", length=1, default="", required=True)
    codigo_carteira = CNABFieldInteger("", length=1, default="1", required=True)
    seu_numero = CNABFieldInteger("", length=11, default="", required=True)
    filler5 = CNABFieldAlfa("", length=4, default=" ", required=True)
    data_vencimento = CNABFieldDate("", length=8, default="", required=True)
    vlr_nominal = CNABFieldDecimal(
        "", length=13, default="0", precision=2, required=True
    )
    cod_banco_receb = CNABFieldAlfa("", length=3, default=" ", required=True)
    agencia_recebedora = CNABFieldInteger("", length=5, default=" ", required=True)
    dv_agencia_receb = CNABFieldInteger("", length=1, default="", required=True)
    seu_numero2 = CNABFieldAlfa("", length=25, default="", required=True)
    codigo_moeda = CNABFieldInteger("", length=2, default="", required=True)
    tipo_inscricao = CNABFieldInteger("", length=1, default="0", required=True)
    numero_inscricao = CNABFieldInteger("", length=15, default="0", required=True)
    nome_pagador = CNABFieldAlfa("", length=40, default="", required=True)
    filler6 = CNABFieldAlfa("", length=10, default="", required=True)
    vlr_tarifa = CNABFieldDecimal("", length=13, default="", precision=2, required=True)
    codigo_ocorrencia = CNABFieldInteger("", length=10, default="0", required=True)
    filler7 = CNABFieldAlfa("", length=17, default="0", required=True)

    def __init__(self, file, line: str):
        super().__init__(file, line)
        self.inserir_detalhe()

    def inserir_detalhe(self):
        instance = CaixaRetornoCnab240Registro3U(
            self.file, self.file._lines[self.file._lines_counter]
        )
        self.children.append(instance)

        next_line = self.file._lines[self.file._lines_counter]
        if next_line[13:14] != "Y":
            return

        if next_line[15:17] != "08":
            return

        instance = CaixaRetornoCnab240Registro3Y08(self.file, next_line)
        self.children.append(instance)
