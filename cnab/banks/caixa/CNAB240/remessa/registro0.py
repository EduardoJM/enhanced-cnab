from cnab.base.remessa.CNAB240 import CNAB240Registro0
from cnab.core.field import (
    CNABCreatedDateField,
    CNABCreatedTimeField,
    CNABFieldAlfa,
    CNABFieldInteger,
)

from .registro1 import Caixa240Registro1


class Caixa240Registro0(CNAB240Registro0):
    registro1_class = Caixa240Registro1

    codigo_banco = CNABFieldInteger("", length=3, default="104", required=True)
    codigo_lote = CNABFieldInteger("", length=4, default="0000", required=True)
    tipo_registro = CNABFieldInteger("", length=1, default="0", required=True)
    filler1 = CNABFieldAlfa("", length=9, default=" ", required=True)
    tipo_inscricao = CNABFieldInteger("", length=1, default="", required=True)
    numero_inscricao = CNABFieldInteger("", length=14, default="", required=True)
    filler2 = CNABFieldInteger("", length=20, default="0", required=True)
    agencia = CNABFieldInteger("", length=5, default="", required=True)
    agencia_dv = CNABFieldInteger("", length=1, default="", required=True)
    codigo_beneficiario = CNABFieldInteger("", length=7, default="", required=True)
    filler3 = CNABFieldInteger("", length=7, default="0", required=True)
    nome_empresa = CNABFieldAlfa("", length=30, default="", required=True)
    nome_banco = CNABFieldAlfa("", length=30, default="CAIXA", required=True)
    filler4 = CNABFieldAlfa("", length=10, default=" ", required=True)
    codigo_remessa = CNABFieldInteger("", length=1, default="1", required=True)
    data_geracao = CNABCreatedDateField("", length=8, required=True)
    hora_geracao = CNABCreatedTimeField("", length=6, required=True)
    numero_sequencial_arquivo = CNABFieldInteger(
        "", length=6, default="", required=True
    )
    versao_layout = CNABFieldInteger("", length=3, default="101", required=True)
    densidade_gravacao = CNABFieldInteger("", length=5, default="0", required=True)
    filler5 = CNABFieldAlfa("", length=20, default=" ", required=True)
    reservado_empresa = CNABFieldAlfa("", length=20, default=" ", required=True)
    filler6 = CNABFieldAlfa("", length=4, default=" ", required=True)
    filler7 = CNABFieldAlfa("", length=25, default=" ", required=True)

    def get_versao_layout(self):
        # TODO: change this in future
        if self.versao_layout:
            return self.versao_layout

        if len(self.codigo_beneficiario) > 6:
            return "107"
        return "101"

    def get_codigo_beneficiario(self):
        # TODO: change this in future
        versao_layout = self.get_versao_layout()
        if versao_layout == "101":
            code = str(self.codigo_beneficiario).rjust(6, "0")
            return f"{code}0"
        if versao_layout == "107":
            return str(self.codigo_beneficiario).rjust(7, "0")
        # TODO: raise exception here
