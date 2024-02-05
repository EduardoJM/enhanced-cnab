from cnab.base.cnab_240 import CNAB240Registro0
from cnab.core.field import CNABField, CNABFieldType
from .registro1 import Santander240Registro1

class Santander240Registro0(CNAB240Registro0):
    registro1_class = Santander240Registro1
    _meta = {
        "codigo_banco": CNABField(
            length=3,
            default="033",
            validation=CNABFieldType.Int,
            required=True,
        ),
        "codigo_lote": CNABField(
            length=4,
            default="0000",
            validation=CNABFieldType.Int,
            required=True,
        ),
        "tipo_registro": CNABField(
            length=1,
            default="0",
            validation=CNABFieldType.Int,
            required=True,
        ),
        "filler1": CNABField(
            length=8,
            default=" ",
            validation=CNABFieldType.Alfa,
            required=True,
        ),
        "tipo_inscricao": CNABField(
            length=1,
            default="",
            validation=CNABFieldType.Int,
            required=True,
        ),
        "numero_inscricao": CNABField(
            length=15,
            default="",
            validation=CNABFieldType.Int,
            required=True,
        ),
        "agencia": CNABField(
            length=4,
            default="",
            validation=CNABFieldType.Int,
            required=True,
        ),
        "filler12": CNABField(
            length=4,
            default="0",
            validation=CNABFieldType.Int,
            required=True,
        ),
        "codigo_beneficiario": CNABField(
            length=6,
            default="0",
            validation=CNABFieldType.Int,
            required=True,
        ),
        "codigo_beneficiario_dv": CNABField(
            length=1,
            default="0",
            validation=CNABFieldType.Int,
            required=True,
        ),
        "filler2": CNABField(
            length=25,
            default=" ",
            validation=CNABFieldType.Alfa,
            required=True,
        ),
        "nome_empresa": CNABField(
            length=30,
            default="",
            validation=CNABFieldType.Alfa,
            required=True,
        ),
        "nome_banco": CNABField(
            length=30,
            default="BANCO SANTANDER",
            validation=CNABFieldType.Alfa,
            required=True,
        ),
        "filler3": CNABField(
            length=10,
            default=" ",
            validation=CNABFieldType.Alfa,
            required=True,
        ),
        "codigo_remessa": CNABField(
            length=1,
            default="1",
            validation=CNABFieldType.Int,
            required=True,
        ),
        "data_geracao": CNABField(
            length=8,
            default="",
            validation=CNABFieldType.Date,
            required=True,
        ),
        "filler4": CNABField(
            length=6,
            default=" ",
            validation=CNABFieldType.Alfa,
            required=True,
        ),
        "numero_sequencial_arquivo": CNABField(
            length=6,
            default="",
            validation=CNABFieldType.Int,
            required=True,
        ),
        "versao_layout": CNABField(
            length=3,
            default="040",
            validation=CNABFieldType.Int,
            required=True,
        ),
        "filler5": CNABField(
            length=74,
            default=" ",
            validation=CNABFieldType.Alfa,
            required=True,
        ),
    }
