from typing import Optional, Union
from cnab.base.cnab_240 import CNAB240Registro0
from cnab.core.field import (
    CNABField,
    CNABFieldType,
    CNABCreatedDateField,
)
from cnab.utils.dict_utils import set_if_has_value
from .registro1 import Caixa240Registro1


class Caixa240Registro0(CNAB240Registro0):
    registro1_class = Caixa240Registro1
    _meta = {
        "codigo_banco": CNABField(  # 01.0
            length=3,
            default="104",
            validation=CNABFieldType.Int,
            required=True
        ),
        "codigo_lote": CNABField(  # 02.0
            length=4, default="0000", validation=CNABFieldType.Int, required=True
        ),
        "tipo_registro": CNABField(  # 03.0
            length=1, default="0", validation=CNABFieldType.Int, required=True
        ),
        "filler1": CNABField(  #  04.0
            length=9, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "tipo_inscricao": CNABField(  # 05.0
            length=1, default="", validation=CNABFieldType.Int, required=True
        ),
        "numero_inscricao": CNABField(  # 06.0
            length=14, default="", validation=CNABFieldType.Int, required=True
        ),
        "convenio_caixa": CNABField(  # 07.0
            length=6, default="", validation=CNABFieldType.Int, required=True
        ),
        "param_transmissao": CNABField(  # 07.0
            length=2, default="0", validation=CNABFieldType.Int, required=True
        ),
        "amb_cliente": CNABField(  # 07.0
            length=1,
            default="T",  # T teste e P producao
            validation=CNABFieldType.Alfa,
            required=True,
        ),
        "amb_caixa": CNABField(  # 07.0
            length=1, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "orig_app": CNABField(  # 07.0
            length=3, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "num_versao": CNABField(  # 07.0
            length=4, default="0", validation=CNABFieldType.Int, required=True
        ),
        "filler2": CNABField(  # 07.0
            length=3, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "agencia": CNABField(  # 08.0
            length=5, default="", validation=CNABFieldType.Int, required=True
        ),
        "agencia_dv": CNABField(  # 09.0
            length=1, default="", validation=CNABFieldType.Int, required=True
        ),
        "conta": CNABField(  # 10.0
            length=12, default="0", validation=CNABFieldType.Int, required=True
        ),
        "conta_dv": CNABField(  # 11.0
            length=1, default="7", validation=CNABFieldType.Alfa, required=True
        ),
        "filler3": CNABField(  # 12.0
            length=1, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "nome_empresa": CNABField(  # 13.0
            length=30, default="", validation=CNABFieldType.Alfa, required=True
        ),
        "nome_banco": CNABField(  # 14.0
            length=30, default="CAIXA", validation=CNABFieldType.Alfa, required=True
        ),
        "filler4": CNABField(  # 15.0
            length=10, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "codigo_remessa": CNABField(  # 16.0
            length=1, default="1", validation=CNABFieldType.Int, required=True
        ),
        "data_geracao": CNABCreatedDateField(  # 17.0
            length=8,
            validation=CNABFieldType.Date,
            required=True,
        ),
        "hora_geracao": CNABCreatedDateField(  # 18.00
            length=6,
            validation=CNABFieldType.Int,
            required=True,
        ),
        "numero_sequencial_arquivo": CNABField(  # 19.0
            length=6, default="", validation=CNABFieldType.Int, required=True
        ),
        "versao_layout": CNABField(  # 20.0
            length=3, default="080", validation=CNABFieldType.Int, required=True
        ),
        "densidade_gravacao": CNABField(  # 21.0
            length=5, default="01600", validation=CNABFieldType.Int, required=True
        ),
        "filler5": CNABField(  # 22.0
            length=20, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "reservado_empresa": CNABField(  # 23.0
            length=20, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "filler6": CNABField(  # 24.0
            length=11, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "filler7": CNABField(  # 24.0
            length=3, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "filler8": CNABField(  # 24.0
            length=3, default="0", validation=CNABFieldType.Int, required=True
        ),
        "filler9": CNABField(  # 24.0
            length=2, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "filler10": CNABField(  # 24.0
            length=10, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
    }
