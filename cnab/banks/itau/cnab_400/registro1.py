from typing import Optional, Union
from cnab.base.cnab_400 import CNAB400Registro1
from cnab.core.field import CNABField, CNABFieldType
from cnab.utils.dict_utils import set_if_has_value
from cnab.base.registro import Registro
from .registro2 import ItauCnab400Registro2


class ItauCnab400Registro1(CNAB400Registro1):
    _meta = {
        "tipo_registro": CNABField(
            length=1, default="1", validation=CNABFieldType.Int, required=True
        ),
        "tipo_inscricao_empresa": CNABField(
            length=2, default="", validation=CNABFieldType.Int, required=True
        ),
        "numero_inscricao_empresa": CNABField(
            length=14, default="", validation=CNABFieldType.Int, required=True
        ),
        "agencia": CNABField(
            length=4, default="", validation=CNABFieldType.Int, required=True
        ),
        "filler1": CNABField(
            length=2, default="0", validation=CNABFieldType.Int, required=True
        ),
        "conta": CNABField(
            length=5, default="", validation=CNABFieldType.Int, required=True
        ),
        "conta_dv": CNABField(
            length=1, default="", validation=CNABFieldType.Int, required=True
        ),
        "filler2": CNABField(
            length=4, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "cod_intrucao": CNABField(
            length=4, default="0", validation=CNABFieldType.Int, required=True
        ),
        "seu_numero": CNABField(
            length=25, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "nosso_numero": CNABField(
            length=8, default="", validation=CNABFieldType.Int, required=True
        ),
        "qtd_moeda": CNABField(  # 34.3P
            length=8,
            default="0",
            validation=CNABFieldType.Decimal,
            precision=5,
            required=True,
        ),
        "carteira_banco": CNABField(  # 13.3P
            length=3, default="0", validation=CNABFieldType.Int, required=True
        ),
        "filler3": CNABField(
            length=21, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "cod_carteira": CNABField(  # 13.3P
            length=1, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "codigo_movimento": CNABField(  # codigo da ocorrencia no manual itau
            length=2,
            default="01",  # entrada de titulo
            validation=CNABFieldType.Int,
            required=True,
        ),
        "numero_documento": CNABField(
            length=10,
            default=" ",
            validation=CNABFieldType.Alfa,
            required=True,
        ),
        "data_vencimento": CNABField(  # 20.3
            length=6, default="", validation=CNABFieldType.Date, required=True
        ),
        "valor": CNABField(  # 21.3P
            length=11,
            default="",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "codigo_banco": CNABField(
            length=3, default="341", validation=CNABFieldType.Int, required=True
        ),
        "agencia_cobradora": CNABField(  # 22.3P
            length=5, default="0", validation=CNABFieldType.Int, required=True
        ),
        "especie_titulo": CNABField(  # 24.3P
            length=2, default="2", validation=CNABFieldType.Int, required=True
        ),
        "aceite": CNABField(  # 25.3P
            length=1, default="N", validation=CNABFieldType.Alfa, required=True
        ),
        "data_emissao": CNABField(  # 26.3P
            length=6, default="", validation=CNABFieldType.Date, required=True
        ),
        "cod_instrucao1": CNABField(  # 24.3P
            length=2, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "cod_instrucao2": CNABField(  # 24.3P
            length=2, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "vlr_juros": CNABField(  # 29.3P
            length=11,
            default="0",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "data_desconto": CNABField(  # 31.3P
            length=6, default="0", validation=CNABFieldType.Date, required=True
        ),
        "vlr_desconto": CNABField(  # 32.3P
            length=11,
            default="0",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "vlr_IOF": CNABField(  # 33.3P
            length=11,
            default="0",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "vlr_abatimento": CNABField(  # 34.3P
            length=11,
            default="0",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "tipo_inscricao": CNABField(
            length=2, default="", validation=CNABFieldType.Int, required=True
        ),
        "numero_inscricao": CNABField(
            length=14, default="", validation=CNABFieldType.Int, required=True
        ),
        "nome_pagador": CNABField(  # 10.3Q
            length=30, default="", validation=CNABFieldType.Alfa, required=True
        ),
        "filler4": CNABField(
            length=10, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "endereco_pagador": CNABField(  # 11.3Q
            length=40, default="", validation=CNABFieldType.Alfa, required=True
        ),
        "bairro_pagador": CNABField(  # 12.3Q
            length=12, default="", validation=CNABFieldType.Alfa, required=True
        ),
        "cep_pagador": CNABField(  # 13.3Q
            length=8, default="", validation=CNABFieldType.Int, required=True
        ),
        "cidade_pagador": CNABField(  # 15.3Q
            length=15, default="", validation=CNABFieldType.Alfa, required=True
        ),
        "uf_pagador": CNABField(  # 16.3Q
            length=2,
            default="",  # combrança com registro
            validation=CNABFieldType.Alfa,
            required=True,
        ),
        "nome_avalista": CNABField(  # 18.3Q
            length=30, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "filler5": CNABField(
            length=4, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "data_mora": CNABField(  # 31.3P
            length=6, default="0", validation=CNABFieldType.Date, required=True
        ),
        "prazo_baixa": CNABField(  # 31.3P
            length=2, default="0", validation=CNABFieldType.Int, required=True
        ),
        "filler6": CNABField(
            length=1, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "numero_registro": CNABField(  # 4.3R
            length=6, default="0", validation=CNABFieldType.Int, required=True
        ),
    }

    def __init__(self, header: Optional[Registro], parent: Optional[Registro], **kwargs: dict):
        super().__init__(header, parent, **kwargs)
        self.inserir_multa(**kwargs)

    def inserir_multa(self, **kwargs: dict):
        if not kwargs.get('data_multa'):
            return
        ItauCnab400Registro2(self.header, self, **kwargs)

    def get_agencia_cobradora(self):
        return self.get_data_or_parent('agencia')
