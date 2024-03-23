from cnab.base.cnab_400 import CNAB400Registro0
from cnab.core.field import (
    CNABCreatedDateField,
    CNABFieldInteger,
    CNABFieldAlfa,
)

class ItauCnab400Registro0(CNAB400Registro0):
    tipo_registro = CNABFieldInteger("001-002", length=1, default="0", required=True)
    operacao = CNABFieldInteger("002-002", length=1, default="1", required=True)
    literal_remessa = CNABFieldAlfa("003-009", length=7, default="remessa", required=True)
    tipo_servico = CNABFieldInteger("010-011", length=2, default="01", required=True)
    literal_servico = CNABFieldAlfa("012-026", length=15, default="COBRANCA", required=True)
    agencia = CNABFieldInteger("027-030", length=4, default="", required=True)
    filler1 = CNABFieldInteger("031-032", length=2, default="0", required=True)
    conta = CNABFieldInteger("033-037", length=5, default="", required=True)
    conta_dv = CNABFieldInteger("038-038", length=1, default="", required=True)
    filler2 = CNABFieldAlfa("039-046", length=8, default=" ", required=True)
    nome_empresa = CNABFieldAlfa("047-076", length=30, default=" ", required=True)
    codigo_banco = CNABFieldInteger("077-079", length=3, default="341", required=True)
    nome_banco = CNABFieldAlfa("080-094", length=15, default="BANCO ITAU SA", required=True)
    data_gravacao = CNABCreatedDateField("095-100", length=6, required=True)
    filler3 = CNABFieldAlfa("100-394", length=294, default=" ", required=True)
    numero_sequencial = CNABFieldInteger("395-400", length=6, default="1", required=True)

    def inserir_detalhe(self, **kwargs):
        from .registro1 import ItauCnab400Registro1
        return ItauCnab400Registro1(self, self, **kwargs)
