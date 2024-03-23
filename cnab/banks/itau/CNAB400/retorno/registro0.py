from typing import List
from cnab.base.retorno.CNAB400 import Registro0Retorno
from cnab.core.field import (
    CNABFieldInteger,
    CNABFieldAlfa,
    CNABFieldDate,
)
from .registro1 import ItauRetornoCnab400Registro1


class ItauRetornoCnab400Registro0(Registro0Retorno):
    registro1_class = ItauRetornoCnab400Registro1
    children: List[ItauRetornoCnab400Registro1]

    tipo_registro = CNABFieldInteger("001-001", length=1, default="0", required=True)
    operacao = CNABFieldInteger("002-002", length=1, default="2", required=True)
    literal_remessa = CNABFieldAlfa("003-009", length=7, default="RETORNO", required=True)
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
    data_gravacao = CNABFieldDate("095-100", length=6, default="", required=True)
    filler3 = CNABFieldAlfa("101-394", length=294, default=" ", required=True)
    numero_sequencial_arquivo = CNABFieldInteger("395-400", length=6, default="", required=True)
