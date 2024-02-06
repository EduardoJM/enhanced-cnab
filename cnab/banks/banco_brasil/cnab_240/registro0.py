from typing import Optional, Union
from cnab.base.cnab_240 import CNAB240Registro0
from cnab.core.field import CNABField, CNABFieldType
from .registro1 import BancoBrasil240Registro1

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

    def __init__(
        self,
        *,
        codigo_banco: Optional[Union[str, int]] = "001",
        codigo_lote: Optional[Union[str, int]] = "0000",
        tipo_registro: Optional[Union[str, int]] = "0",
        tipo_inscricao: Optional[Union[str, int]] = "0",
        numero_inscricao: Optional[Union[str, int]] = "0",
        convenio: Optional[Union[str, int]] = "0",
        cobranca_cedente: Optional[Union[str, int]] = "0014",
        carteira_cobranca: Optional[Union[str, int]] = "11",
        variacao_carteira_cobranca: Optional[Union[str, int]] = "222",
        agencia: Optional[Union[str, int]] = "0",
        agencia_dv: Optional[Union[str, int]] = "",
        conta: Optional[Union[str, int]] = "0",
        conta_dv: Optional[Union[str, int]] = "0",
        nome_empresa: Optional[str] = "",
        nome_banco: Optional[str] = "BANCO DO BRASIL S.A",
        codigo_remessa: Optional[Union[str, int]] = "1",
        numero_sequencial_arquivo: Optional[Union[str, int]] = "0",
        **kwargs
    ):
        kwargs.set('codigo_banco', codigo_banco)
        kwargs.set('codigo_lote', codigo_lote)
        kwargs.set('tipo_registro', tipo_registro)
        kwargs.set('tipo_inscricao', tipo_inscricao)
        kwargs.set('numero_inscricao', numero_inscricao)
        kwargs.set('convenio', convenio)
        kwargs.set('cobranca_cedente', cobranca_cedente)
        kwargs.set('carteira_cobranca', carteira_cobranca)
        kwargs.set('variacao_carteira_cobranca', variacao_carteira_cobranca)
        kwargs.set('agencia', agencia)
        kwargs.set('agencia_dv', agencia_dv)
        kwargs.set('conta', conta)
        kwargs.set('conta_dv', conta_dv)
        kwargs.set('nome_empresa', nome_empresa)
        kwargs.set('nome_banco', nome_banco)
        kwargs.set('codigo_remessa', codigo_remessa)
        kwargs.set('numero_sequencial_arquivo', numero_sequencial_arquivo)
        super().__init__(**kwargs)
