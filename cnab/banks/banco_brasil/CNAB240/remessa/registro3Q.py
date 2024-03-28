from cnab.base.remessa.CNAB240 import CNAB240Registro3
from cnab.core.field import CNABFieldInteger, CNABFieldAlfa


class BancoBrasil240Registro3Q(CNAB240Registro3):
    codigo_banco = CNABFieldInteger("", length=3, default="001", required=True)
    codigo_lote = CNABFieldInteger("", length=4, default=1, required=True)
    tipo_registro = CNABFieldInteger("", length=1, default="3", required=True)
    numero_registro = CNABFieldInteger("", length=5, default="2", required=True)
    seguimento = CNABFieldAlfa("", length=1, default="Q", required=True)
    filler1 = CNABFieldAlfa("", length=1, default=" ", required=True)
    codigo_movimento = CNABFieldInteger("", length=2, default="01", required=True)
    tipo_inscricao = CNABFieldInteger("", length=1, default="0", required=True)
    numero_inscricao = CNABFieldInteger("", length=15, default="0", required=True)
    nome_pagador = CNABFieldAlfa("", length=40, default="", required=True)
    endereco_pagador = CNABFieldAlfa("", length=40, default="", required=True)
    bairro_pagador = CNABFieldAlfa("", length=15, default="", required=True)
    cep_pagador = CNABFieldInteger("", length=8, default="0", required=True)
    cidade_pagador = CNABFieldAlfa("", length=15, default="", required=True)
    uf_pagador = CNABFieldAlfa("", length=2, default="", required=True)
    tipo_incricao_avalista = CNABFieldInteger("", length=1, default="0", required=True)
    numero_incricao_avalista = CNABFieldInteger(
        "", length=15, default="0", required=True
    )
    nome_avalista = CNABFieldAlfa("", length=40, default=" ", required=True)
    codigo_banco_correspondente = CNABFieldInteger(
        "", length=3, default="0", required=True
    )
    nosso_numero_banco_correspondente = CNABFieldAlfa(
        "", length=20, default=" ", required=True
    )
    filler4 = CNABFieldAlfa("", length=8, default=" ", required=True)
