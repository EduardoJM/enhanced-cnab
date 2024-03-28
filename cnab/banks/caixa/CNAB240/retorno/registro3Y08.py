from cnab.base.retorno.CNAB240 import Registro3Retorno
from cnab.core.field import CNABFieldAlfa, CNABFieldInteger


class CaixaRetornoCnab240Registro3Y08(Registro3Retorno):
    codigo_banco = CNABFieldInteger("", length=3, default="104", required=True)
    codigo_lote = CNABFieldInteger("", length=4, default=1, required=True)
    tipo_registro = CNABFieldInteger("", length=1, default="3", required=True)
    numero_registro = CNABFieldInteger("", length=5, default="0", required=True)
    seguimento = CNABFieldAlfa("", length=1, default="U", required=True)
    filler1 = CNABFieldInteger("", length=1, default=" ", required=True)
    codigo_movimento = CNABFieldInteger("", length=2, default="", required=True)
    identificacao_registro = CNABFieldInteger("", length=2, default="", required=True)
    codigo_solicitacao = CNABFieldInteger("", length=2, default="", required=True)
    id_identificador = CNABFieldInteger("", length=1, default="", required=True)
    numero_solicitacao = CNABFieldInteger("", length=18, default="", required=True)
    descricao = CNABFieldAlfa("", length=180, default="", required=True)
    quantidade = CNABFieldInteger("", length=4, default="", required=True)
    erro = CNABFieldInteger("", length=3, default=" ", required=True)
    filler2 = CNABFieldAlfa("", length=30, default="", required=True)
