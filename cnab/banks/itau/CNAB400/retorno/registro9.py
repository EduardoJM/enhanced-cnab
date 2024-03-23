from cnab.base.retorno.CNAB400 import Registro9Retorno
from cnab.core.field import CNABFieldInteger, CNABFieldAlfa, CNABFieldDecimal


class ItauRetornoCnab400Registro9(Registro9Retorno):
    tipo_registro = CNABFieldInteger("001-001", length=1, default="9", required=True)
    codigo_retorno = CNABFieldInteger("002-002", length=1, default="2", required=True)
    codigo_servico = CNABFieldInteger("003-004", length=2, default="01", required=True)
    codigo_banco = CNABFieldInteger("005-007", length=3, default="341", required=True)
    filler1 = CNABFieldAlfa("008-017", length=10, default=" ", required=True)
    qtde_titulos_simples = CNABFieldInteger("018-025", length=8, default=0, required=True)
    valor_total_simples = CNABFieldDecimal("026-039", length=12, precision=2, default=0, required=True)
    aviso_bancario_simples = CNABFieldAlfa("040-047", length=8, default=" ", required=True)
    filler2 = CNABFieldAlfa("048-057", length=10, default=" ", required=True)
    qtde_titulos_vinculada = CNABFieldInteger("058-065", length=8, default=0, required=True)
    valor_total_vinculada = CNABFieldDecimal("066-079", length=12, precision=2, default=0, required=True)
    aviso_bancario_vinculada = CNABFieldAlfa("080-087", length=8, default=" ", required=True)
    filler3 = CNABFieldAlfa("088-177", length=90, default=" ", required=True)
    qtde_titulos_direta = CNABFieldInteger("178-185", length=8, default=0, required=True)
    valor_total_direta = CNABFieldDecimal("186-99", length=12, precision=2, default=0, required=True)
    aviso_bancario_direta = CNABFieldAlfa("200-207", length=8, default=" ", required=True)
    sequencial_arquivo_retorno = CNABFieldInteger("208-212", length=5, default="0", required=True)
    quantidade_detalhes = CNABFieldInteger("213-220", length=8, default="0", required=True)
    valor_total = CNABFieldDecimal("221-234", length=12, precision=2, default=0, required=True)
    filler4 = CNABFieldAlfa("235-394", length=160, default=" ", required=True)
    numero_registro = CNABFieldInteger("395-400", length=6, default="0", required=True)
