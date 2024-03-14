from cnab.base.cnab_240 import CNAB240Registro3
from cnab.core.field import CNABField, CNABFieldType


class BancoBrasil240Registro3Q(CNAB240Registro3):
    _meta = {
        "codigo_banco": CNABField(  # 1.3Q
            length=3, default="001", validation=CNABFieldType.Int, required=True
        ),
        "codigo_lote": CNABField(  # 2.3Q
            length=4, default=1, validation=CNABFieldType.Int, required=True
        ),
        "tipo_registro": CNABField(  # 3.3Q
            length=1, default="3", validation=CNABFieldType.Int, required=True
        ),
        "numero_registro": CNABField(  # 4.3Q
            length=5, default="2", validation=CNABFieldType.Int, required=True
        ),
        "seguimento": CNABField(  # 5.3Q
            length=1, default="Q", validation=CNABFieldType.Alfa, required=True
        ),
        "filler1": CNABField(  # 6.3Q
            length=1, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "codigo_movimento": CNABField(  # 7.3Q
            length=2,
            default="01",  # entrada de titulo
            validation=CNABFieldType.Int,
            required=True,
        ),
        # - ------------------ até aqui é igual para todo registro tipo 3
        "tipo_inscricao": CNABField(  # 8.3Q
            length=1, default="0", validation=CNABFieldType.Int, required=True
        ),
        "numero_inscricao": CNABField(  # 9.3Q
            length=15, default="0", validation=CNABFieldType.Int, required=True
        ),
        "nome_pagador": CNABField(  # 10.3Q
            length=40, default="", validation=CNABFieldType.Alfa, required=True
        ),
        "endereco_pagador": CNABField(  # 11.3Q
            length=40, default="", validation=CNABFieldType.Alfa, required=True
        ),
        "bairro_pagador": CNABField(  # 12.3Q
            length=15, default="", validation=CNABFieldType.Alfa, required=True
        ),
        "cep_pagador": CNABField(  # 13.3Q
            length=5, default="0", validation=CNABFieldType.Int, required=True
        ),
        "cep_sufixo": CNABField(  # 14.3Q
            length=3, default="0", validation=CNABFieldType.Int, required=True
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
        "tipo_incricao_avalista": CNABField(  # 17.3Q
            length=1, default="0", validation=CNABFieldType.Int, required=True
        ),
        "numero_incricao_avalista": CNABField(  # 18.3
            length=15, default="0", validation=CNABFieldType.Int, required=True
        ),
        "nome_avalista": CNABField(  # 18.3Q
            length=40, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "codigo_banco_correspondente": CNABField(  # 18.3Q
            length=3, default="0", validation=CNABFieldType.Int, required=True
        ),
        "nosso_numero_banco_correspondente": CNABField(  # 19.3Q   Campo de preenchimento obrigatório; preencher com Seu Número de controle do título
            length=20,
            default=" ",  # este espaço foi colocado para passa a validação para os seters do generico
            validation=CNABFieldType.Alfa,
            required=True,
        ),
        "filler4": CNABField(  # 19.3Q
            length=8, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
    }
