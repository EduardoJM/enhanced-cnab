from typing import List

from cnab.base.retorno.CNAB240 import Registro0Retorno
from cnab.core.field import CNABFieldAlfa, CNABFieldDate, CNABFieldInteger

from .registro1 import CaixaRetornoCnab240Registro1
from .registro5 import CaixaRetornoCnab240Registro5


class CaixaRetornoCnab240Registro0(Registro0Retorno):
    children: List[CaixaRetornoCnab240Registro1]

    codigo_banco = CNABFieldInteger("", length=3, default="104", required=True)
    codigo_lote = CNABFieldInteger("", length=4, default="0000", required=True)
    tipo_registro = CNABFieldInteger("", length=1, default="1", required=True)
    filler1 = CNABFieldAlfa("", length=9, default=" ", required=True)
    tipo_inscricao = CNABFieldInteger("", length=1, default="", required=True)
    numero_inscricao = CNABFieldInteger("", length=14, default="", required=True)
    uso_caixa1 = CNABFieldInteger("", length=20, default="0", required=True)
    agencia = CNABFieldInteger("", length=5, default="", required=True)
    agencia_dv = CNABFieldInteger("", length=1, default="", required=True)
    codigo_beneficiario = CNABFieldInteger("", length=7, default="", required=True)
    uso_caixa2 = CNABFieldInteger("", length=7, default="0", required=True)
    nome_empresa = CNABFieldAlfa("", length=30, default="", required=True)
    nome_banco = CNABFieldAlfa("", length=30, default="", required=True)
    filler3 = CNABFieldAlfa("", length=10, default=" ", required=True)
    codigo_remessa = CNABFieldInteger("", length=1, default="", required=True)
    data_geracao = CNABFieldDate("", length=8, default="", required=True)
    hora_geracao = CNABFieldInteger("", length=6, default="", required=True)
    numero_sequencial_arquivo = CNABFieldInteger(
        "", length=6, default="", required=True
    )
    versao_layout = CNABFieldInteger("", length=3, default="", required=True)
    densidade_gravacao = CNABFieldInteger("", length=5, default="0", required=True)
    filler4 = CNABFieldAlfa("", length=20, default=" ", required=True)
    situacao_arquivo = CNABFieldAlfa("", length=20, default="", required=True)
    versao_aplicativo = CNABFieldAlfa("", length=4, default=" ", required=True)
    filler5 = CNABFieldAlfa("", length=25, default=" ", required=True)

    def __init__(self, file, line: str):
        super().__init__(file, line)
        self.inserir_detalhe()

    def inserir_detalhe(self):
        while self.file._lines_counter < len(self.file._lines) - 4:
            instance = CaixaRetornoCnab240Registro1(
                self.file, self.file._lines[self.file._lines_counter]
            )
            instance.trailler = CaixaRetornoCnab240Registro5(
                self.file, self.file._lines[self.file._lines_counter]
            )
            self.children.append(instance)
