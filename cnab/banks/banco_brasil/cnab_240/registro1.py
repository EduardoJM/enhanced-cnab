from cnab.base.cnab_240 import CNAB240Registro1
from cnab.core.field import CNABField, CNABFieldType
from .registro5 import BancoBrasil240Registro5


class BancoBrasil240Registro1(CNAB240Registro1):
    registro5_class = BancoBrasil240Registro5
    _meta = {
        "codigo_banco": CNABField(  # 01.1
            length=3, default="001", validation=CNABFieldType.Int, required=True
        ),
        "codigo_lote": CNABField(  # 02.1
            length=4, default=1, validation=CNABFieldType.Int, required=True
        ),
        "tipo_registro": CNABField(  # 3.1
            length=1, default=1, validation=CNABFieldType.Int, required=True
        ),
        "operacao": CNABField(  # 04.1
            length=1, default="R", validation=CNABFieldType.Alfa, required=True
        ),
        "tipo_servico": CNABField(  # 05.1
            length=2, default="01", validation=CNABFieldType.Int, required=True
        ),
        "filler1": CNABField(  # 06.1
            length=2, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "versa_layout": CNABField(  # 07.1
            length=3, default="000", validation=CNABFieldType.Int, required=True
        ),
        "filler2": CNABField(  # 08.1
            length=1, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "tipo_inscricao": CNABField(  # 09.1
            length=1, default="0", validation=CNABFieldType.Int, required=True
        ),
        "numero_inscricao": CNABField(  # 10.1
            length=15, default="", validation=CNABFieldType.Int, required=True
        ),
        "convenio": CNABField(  # 11.1
            length=9, default="0", validation=CNABFieldType.Int, required=True
        ),
        "cobranca": CNABField(  # 11.1
            length=4, default="0014", validation=CNABFieldType.Int, required=True
        ),
        "carteira": CNABField(  # 11.1
            length=2, default="0", validation=CNABFieldType.Int, required=True
        ),
        "variacao": CNABField(  # 11.1
            length=3, default="000", validation=CNABFieldType.Int, required=True
        ),
        "situacao_arquivo": CNABField(  # 11.1
            length=2, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "agencia": CNABField(  # 12.1
            length=5, default="", validation=CNABFieldType.Int, required=True
        ),
        "agencia_dv": CNABField(  # 13.1
            length=1, default="", validation=CNABFieldType.Alfa, required=True
        ),
        "conta": CNABField(  # 14.1
            length=12, default="", validation=CNABFieldType.Int, required=True
        ),
        "conta_dv": CNABField(  # 15.1
            length=1, default="", validation=CNABFieldType.Alfa, required=True
        ),
        "filler3": CNABField(  # 16.1
            length=1, default="0", validation=CNABFieldType.Alfa, required=True
        ),
        "nome_empresa": CNABField(  # 17.1
            length=30, default="", validation=CNABFieldType.Alfa, required=True
        ),
        "mensagem_fixa1": CNABField(  # 18.1 mensagems 1 e 2 : somente use para mensagens que serao impressas de forma identica em todos os boletos do lote
            length=40, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "mensagem_fixa2": CNABField(  # 19.1 mensagems 1 e 2 : somente use para mensagens que serao impressas de forma identica em todos os boletos do lote
            length=40, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "numero_remessa": CNABField(  # 20.1
            length=8, default="0", validation=CNABFieldType.Int, required=True
        ),
        "data_gravacao": CNABField(  # 21.1
            length=8,
            default="",  # nao informar a data na instanciação - gerada dinamicamente
            validation=CNABFieldType.Date,
            required=True,
        ),
        "filler4": CNABField(  # 22.1
            length=8, default="0", validation=CNABFieldType.Int, required=True
        ),
        "filler5": CNABField(  # 23.1
            length=33, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
    }

    def inserir_detalhe(self, **kwargs):
        from .registro3P import BancoBrasil240Registro3P
        return BancoBrasil240Registro3P(self.header, self, self, **kwargs)
