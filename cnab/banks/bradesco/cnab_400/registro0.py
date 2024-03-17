from typing import Optional, Union
from cnab.base.cnab_400 import CNAB400Registro0
from cnab.core.field import CNABField, CNABFieldType
from cnab.utils.dict_utils import set_if_has_value


class BradescoCnab400Registro0(CNAB400Registro0):
    _meta = {
        "tipo_registro": CNABField(
            length=1, default="0", validation=CNABFieldType.Int, required=True
        ),
        "operacao": CNABField(
            length=1, default="1", validation=CNABFieldType.Int, required=True
        ),
        "literal_remessa": CNABField(
            length=7, default="remessa", validation=CNABFieldType.Alfa, required=True
        ),
        "tipo_servico": CNABField(
            length=2, default="01", validation=CNABFieldType.Int, required=True
        ),
        "literal_servico": CNABField(
            length=8, default="COBRANÇA", validation=CNABFieldType.Alfa2, required=True
        ),
        "filler0": CNABField(
            length=7, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "agencia": CNABField(
            length=4, default="", validation=CNABFieldType.Int, required=True
        ),
        "agencia_dv": CNABField(
            length=1, default="", validation=CNABFieldType.Int, required=True
        ),
        "codigo_beneficiario": CNABField(
            length=8, default="", validation=CNABFieldType.Int, required=True
        ),
        "codigo_beneficiario_dv": CNABField(
            length=1, default="", validation=CNABFieldType.Alfa, required=True
        ),
        "numero_convenio": CNABField(
            length=6, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "nome_empresa": CNABField(
            length=30, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "codigo_banco": CNABField(
            length=3, default="756", validation=CNABFieldType.Int, required=True
        ),
        "nome_banco": CNABField(
            length=15,
            default="BANCOOBCED",
            validation=CNABFieldType.Alfa,
            required=True,
        ),
        "data_gravacao": CNABField(
            length=6,
            default="",  # nao informar a data na instanciaÃ§Ã£o - gerada dinamicamente
            validation=CNABFieldType.Date,
            required=True,
        ),
        "numero_sequencial_arquivo": CNABField(
            length=7, default="1", validation=CNABFieldType.Int, required=True
        ),
        "filler3": CNABField(
            length=287, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "numero_sequencial": CNABField(
            length=6, default="1", validation=CNABFieldType.Int, required=True
        ),
    }

    def inserir_detalhe(self, **kwargs):
        from .registro1 import BradescoCnab400Registro1
        return BradescoCnab400Registro1(self, self, **kwargs)
