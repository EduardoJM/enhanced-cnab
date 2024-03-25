from cnab.base.cnab_400 import CNAB400Registro0
from cnab.core.field import CNABFieldInteger, CNABFieldAlfa, CNABCreatedDateField


class BradescoCnab400Registro0(CNAB400Registro0):
    identificacao_registro = CNABFieldInteger("001-001", length=1, default='0', required=True)
    operacao = CNABFieldInteger("002-002", length=1, default='1', required=True)
    literal_remessa = CNABFieldAlfa("003-009", length=7, default='remessa', required=True)
    tipo_servico = CNABFieldInteger("010-011", length=2, default='01', required=True)
    literal_servico = CNABFieldAlfa("012-026", length=15, default='COBRANCA', required=True)
    codigo_beneficiario = CNABFieldInteger("027-046", length=20, default='', required=True)
    nome_empresa = CNABFieldAlfa("047-076", length=30, default=' ', required=True)
    codigo_banco = CNABFieldInteger("077-079", length=3, default='237', required=True)
    nome_banco = CNABFieldAlfa("080-094", length=15, default='Bradesco', required=True)
    data_gravacao = CNABCreatedDateField("095-100", length=6, required=True)
    filler1 = CNABFieldAlfa("101-108", length=8, default=' ', required=True)
    identificacao_sistema = CNABFieldAlfa("109-110", length=2, default='MX', required=True)
    numero_sequencial_arquivo = CNABFieldInteger("111-117", length=7, default='1', required=True)
    filler2 = CNABFieldAlfa("118-394", length=277, default=' ', required=True)
    numero_sequencial = CNABFieldInteger("395-400", length=6, default='1', required=True)

    def inserir_detalhe(self, **kwargs):
        from .registro1 import BradescoCnab400Registro1
        return BradescoCnab400Registro1(self, self, **kwargs)
