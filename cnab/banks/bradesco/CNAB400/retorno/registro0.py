from cnab.base.retorno.CNAB400 import Registro0Retorno
from cnab.core.field import CNABFieldInteger, CNABFieldAlfa, CNABFieldDate
from .registro1 import BradescoRetornoCnab400Registro1
from .registro4 import BradescoRetornoCnab400Registro4


class BradescoRetornoCnab400Registro0(Registro0Retorno):
    registro1_class = BradescoRetornoCnab400Registro1

    tipo_registro = CNABFieldInteger("001-001", length=1, default="0", required=True)
    operacao = CNABFieldInteger("002-002", length=1, default="2", required=True)
    literal_retorno = CNABFieldAlfa(
        "003-009", length=7, default="RETORNO", required=True
    )
    tipo_servico = CNABFieldInteger("010-011", length=2, default="01", required=True)
    literal_servico = CNABFieldAlfa(
        "012-026", length=15, default="COBRANCA", required=True
    )
    codigo_empresa = CNABFieldAlfa("027-046", length=20, default="", required=True)
    nome_empresa = CNABFieldAlfa("047-076", length=30, default=" ", required=True)
    codigo_banco = CNABFieldInteger("077-079", length=3, default="237", required=True)
    nome_banco = CNABFieldAlfa("080-094", length=15, default="BRADESCO", required=True)
    data_gravacao = CNABFieldDate("095-100", length=6, default="", required=True)
    densidade_gravacao = CNABFieldInteger(
        "101-108", length=8, default="0", required=True
    )
    n_aviso_bancario = CNABFieldInteger("109-113", length=5, default="", required=True)
    filler1 = CNABFieldAlfa("114-379", length=266, default=" ", required=True)
    data_credito = CNABFieldDate("380-385", length=6, default="", required=True)
    filler2 = CNABFieldAlfa("386-394", length=9, default=" ", required=True)
    numero_sequencial_registro = CNABFieldInteger(
        "395-400", length=6, default="", required=True
    )

    @property
    def has_pix(self):
        return "qrpix.bradesco.com.br" in self.file._lines[2]

    def _parse_pix_child_item(self):
        line = self.file._lines[self.file._lines_counter]
        instance = BradescoRetornoCnab400Registro4(self.file, line)
        self.children.append(instance)

    def _parse_childs(self):
        diff = 3 if self.has_pix else 2

        while self.file._lines_counter < len(self.file._lines) - diff:
            self._parse_child_item()
            self._parse_pix_child_item()
