from cnab.base.cnab_240 import CNAB240Registro1
from cnab.core.field import CNABField, CNABFieldType
from .registro5 import Santander240Registro5

class Santander240Registro1(CNAB240Registro1):
    registro5_class = Santander240Registro5
    _meta = {
        "codigo_banco": CNABField(
            length=3, default="033", validation=CNABFieldType.Int, required=True
        ),
        "codigo_lote": CNABField(
            length=4, default=1, validation=CNABFieldType.Int, required=True
        ),
        "tipo_registro": CNABField(
            length=1, default=1, validation=CNABFieldType.Int, required=True
        ),
        "operacao": CNABField(
            length=1, default="R", validation=CNABFieldType.Alfa, required=True
        ),
        "tipo_servico": CNABField(
            length=2, default="01", validation=CNABFieldType.Int, required=True
        ),
        "filler1": CNABField(
            length=2, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "versao_layout": CNABField(
            length=3, default="030", validation=CNABFieldType.Int, required=True
        ),
        "filler2": CNABField(
            length=1, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "tipo_inscricao": CNABField(
            length=1, default="", validation=CNABFieldType.Int, required=True
        ),
        "numero_inscricao": CNABField(
            length=15, default="", validation=CNABFieldType.Int, required=True
        ),
        "filler3": CNABField(
            length=20, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "agencia": CNABField(
            length=4, default="", validation=CNABFieldType.Int, required=True
        ),
        "filler12": CNABField(
            length=4, default="0", validation=CNABFieldType.Int, required=True
        ),
        "codigo_beneficiario": CNABField(
            length=6, default="0", validation=CNABFieldType.Int, required=True
        ),
        "codigo_beneficiario_dv": CNABField(
            length=1, default="0", validation=CNABFieldType.Int, required=True
        ),
        "filler4": CNABField(
            length=5, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "nome_empresa": CNABField(
            length=30, default="", validation=CNABFieldType.Alfa, required=True
        ),
        "mensagem1": CNABField(
            # mensagems 1 e 2 : somente use para mensagens que serao impressas de forma identica em todos os boletos do lote
            length=40,
            default=" ",
            validation=CNABFieldType.Alfa,
            required=True,
        ),
        "mensagem2": CNABField(
            # mensagems 1 e 2 : somente use para mensagens que serao impressas de forma identica em todos os boletos do lote
            length=40,
            default=" ",
            validation=CNABFieldType.Alfa,
            required=True,
        ),
        "numero_remessa": CNABField(
            length=8, default="", validation=CNABFieldType.Int, required=True
        ),
        "data_gravacao": CNABField(
            length=8,
            default="",  # nao informar a data na instanciação - gerada dinamicamente
            validation=CNABFieldType.Date,
            required=True,
        ),
        "filler5": CNABField(
            length=41, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
    }

    def inserir_detalhe(self, **kwargs):
        from .registro3P import Santander240Registro3P
        return Santander240Registro3P(self.header, self, self, **kwargs)