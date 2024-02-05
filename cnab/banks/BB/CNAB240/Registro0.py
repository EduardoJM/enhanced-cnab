from cnab.base.layouts.CNAB240 import CNAB240Registro0
from cnab.core.field import CNABField, CNABFieldType
from .Registro1 import BancoBrasil240Registro1

class BancoBrasil240Registro0(CNAB240Registro0):
    registro1_class = BancoBrasil240Registro1
    _meta = {
        "codigo_banco": CNABField(  # 01.0
            length=3, default="001", validation=CNABFieldType.Int, required=True
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
            length=1, default="0", validation=CNABFieldType.Int, required=True
        ),
        "numero_inscricao": CNABField(  # 06.0
            length=14, default="0", validation=CNABFieldType.Int, required=True
        ),
        "convenio": CNABField(  # 07.0 BB1
            length=9, default="0", validation=CNABFieldType.Int, required=True
        ),
        "cobranca_cedente": CNABField(  # 07.0 BB2
            length=4, default="0014", validation=CNABFieldType.Int, required=True
        ),
        "carteira_cobranca": CNABField(  # 07.0 BB3
            length=2, default="11", validation=CNABFieldType.Int, required=True
        ),
        "variacao_carteira_cobranca": CNABField(  # 07.0 BB4
            length=3, default="222", validation=CNABFieldType.Int, required=True
        ),
        "reservado_bb": CNABField(  # 07.0 BB5
            length=2, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "agencia": CNABField(  # 08.0
            length=5, default="0", validation=CNABFieldType.Int, required=True
        ),
        "agencia_dv": CNABField(  # 09.0
            length=1, default="", validation=CNABFieldType.Alfa, required=True
        ),
        "conta": CNABField(  # 10.0
            length=12, default="0", validation=CNABFieldType.Int, required=True
        ),
        "conta_dv": CNABField(  # 11.0
            length=1, default="0", validation=CNABFieldType.Alfa, required=True
        ),
        "filler2": CNABField(  # 12.0
            length=1, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "nome_empresa": CNABField(  # 13.0
            length=30, default="", validation=CNABFieldType.Alfa, required=True
        ),
        "nome_banco": CNABField(  # 14.0
            length=30,
            default="BANCO DO BRASIL S.A",
            validation=CNABFieldType.Alfa,
            required=True,
        ),
        "filler3": CNABField(  # 15.0
            length=10, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "codigo_remessa": CNABField(  # 16.0
            length=1, default="1", validation=CNABFieldType.Int, required=True
        ),
        "data_geracao": CNABField(  # 17.0
            length=8,
            default="",  # nao informar a data na instanciaÃ§Ã£o - gerada dinamicamente
            validation=CNABFieldType.Date,
            required=True,
        ),
        "hora_geracao": CNABField(  # 18.00
            length=6,
            default="",  # nao informar a data na instanciaÃ§Ã£o - gerada dinamicamente
            validation=CNABFieldType.Time,
            required=True,
        ),
        "numero_sequencial_arquivo": CNABField(  # 19.0
            length=6, default="0", validation=CNABFieldType.Int, required=True
        ),
        "versao_layout": CNABField(  # 20.0
            length=3, default="000", validation=CNABFieldType.Int, required=True
        ),
        "densidade_gravacao": CNABField(  # 21.0
            length=5, default="0", validation=CNABFieldType.Int, required=True
        ),
        "filler4": CNABField(  # 22.0
            length=20, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "situacao_arquivo2": CNABField(  # 23.0
            length=20, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "filler5": CNABField(
            length=14, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "filler6": CNABField(  # Caso a versão do leiaute seja 30,
            length=3,  # Deve ser preenchido com 'zeros' nas posições 226 a 228.
            default="000",
            validation=CNABFieldType.Alfa,
            required=True,
        ),
        "filler7": CNABField(
            length=12, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
    }
