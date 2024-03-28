from typing import List

from cnab.base.retorno.CNAB240 import Registro1Retorno
from cnab.core.field import CNABFieldAlfa, CNABFieldDate, CNABFieldInteger

from .registro3T import CaixaRetornoCnab240Registro3T
from .registro5 import CaixaRetornoCnab240Registro5


class CaixaRetornoCnab240Registro1(Registro1Retorno):
    trailler: CaixaRetornoCnab240Registro5
    children: List[CaixaRetornoCnab240Registro3T]

    codigo_banco = CNABFieldInteger("", length=3, default="104", required=True)
    codigo_lote = CNABFieldInteger("", length=4, default=1, required=True)
    tipo_registro = CNABFieldInteger("", length=1, default=1, required=True)
    operacao = CNABFieldAlfa("", length=1, default="", required=True)
    tipo_servico = CNABFieldInteger("", length=2, default="", required=True)
    filler1 = CNABFieldInteger("", length=2, default="0", required=True)
    versa_layout = CNABFieldInteger("", length=3, default="030", required=True)
    filler2 = CNABFieldAlfa("", length=1, default="", required=True)
    tipo_inscricao = CNABFieldInteger("", length=1, default="", required=True)
    numero_inscricao = CNABFieldInteger("", length=15, default="", required=True)
    codigo_beneficiario = CNABFieldInteger("", length=7, default="", required=True)
    uso_caixa1 = CNABFieldInteger("", length=13, default="0", required=True)
    agencia = CNABFieldInteger("", length=5, default="", required=True)
    agencia_dv = CNABFieldInteger("", length=1, default="", required=True)
    uso_caixa2 = CNABFieldInteger("", length=6, default="", required=True)
    modelo_boleto = CNABFieldInteger("", length=7, default="", required=True)
    uso_caixa3 = CNABFieldInteger("", length=1, default="0", required=True)
    nome_empresa = CNABFieldAlfa("", length=30, default="", required=True)
    mensagem_fixa1 = CNABFieldAlfa("", length=40, default=" ", required=True)
    mensagem_fixa2 = CNABFieldAlfa("", length=40, default=" ", required=True)
    numero_remessa = CNABFieldInteger("", length=8, default="", required=True)
    data_gravacao = CNABFieldDate("", length=8, default="", required=True)
    data_credito = CNABFieldDate("", length=8, default="0", required=True)
    filler4 = CNABFieldAlfa("", length=33, default=" ", required=True)

    def __init__(self, file, line: str):
        super().__init__(file, line)
        self.inserir_detalhe()

    def inserir_detalhe(self):
        while True:
            next_line = self.file._lines[self.file._lines_counter]
            if int(self.codigo_lote) != int(next_line[3:7]):
                break
            if next_line[13:14] != "T":
                break

            instance = CaixaRetornoCnab240Registro3T(
                self.file, self.file._lines[self.file._lines_counter]
            )
            self.children.append(instance)
