from typing import Optional
from cnab.base.cnab_240 import CNAB240Registro3
from cnab.core.field import CNABField, CNABFieldType
from cnab.base.registro import Registro
from .registro3Q import BancoBrasil240Registro3Q
from .registro3R import BancoBrasil240Registro3R
from .registro3S1e2 import BancoBrasil240Registro3S1e2
from .registro3S3 import BancoBrasil240Registro3S3
from .registro1 import BancoBrasil240Registro1
from .registro0 import BancoBrasil240Registro0


class BancoBrasil240Registro3P(CNAB240Registro3):
    _meta = {
        "codigo_banco": CNABField(  # 1.3P
            length=3, default="001", validation=CNABFieldType.Int, required=True
        ),
        "codigo_lote": CNABField(  # 2.3P
            length=4, default=1, validation=CNABFieldType.Int, required=True
        ),
        "tipo_registro": CNABField(  # 3.3P
            length=1, default="3", validation=CNABFieldType.Int, required=True
        ),
        "numero_registro": CNABField(  # 4.3P
            length=5, default="0", validation=CNABFieldType.Int, required=True
        ),
        "seguimento": CNABField(  # 5.3P
            length=1, default="P", validation=CNABFieldType.Alfa, required=True
        ),
        "filler1": CNABField(  # 6.3P
            length=1, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "codigo_movimento": CNABField(  # 7.3P
            length=2,
            default="01",  # entrada de titulo
            validation=CNABFieldType.Int,
            required=True,
        ),
        # - ------------------ até aqui é igual para todo registro tipo 3
        "agencia": CNABField(  # 8.3P
            length=5, default="0", validation=CNABFieldType.Int, required=True
        ),
        "agencia_dv": CNABField(  # 9.3P
            length=1, default="", validation=CNABFieldType.Alfa, required=True
        ),
        "conta": CNABField(  # 10.3P
            length=12, default="0", validation=CNABFieldType.Int, required=True
        ),
        "conta_dv": CNABField(  # 11.3P
            length=1, default="0", validation=CNABFieldType.Alfa, required=True
        ),
        "filler2": CNABField(  # 12.3P
            length=1, default="0", validation=CNABFieldType.Alfa, required=True
        ),
        "nosso_numero": CNABField(  # 13.3P
            length=20, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "codigo_carteira": CNABField(  # 14.3P
            length=1, default="0", validation=CNABFieldType.Int, required=True
        ),
        "com_registro": CNABField(  # 15.3P
            length=1,
            default="1",  # combrança com registro
            validation=CNABFieldType.Int,
            required=True,
        ),
        "tipo_documento": CNABField(  # 16.3P
            length=1, default="2", validation=CNABFieldType.Int, required=True
        ),
        "emissao_boleto": CNABField(  # 17.3
            length=1, default="2", validation=CNABFieldType.Int, required=True
        ),
        "entrega_boleto": CNABField(  # 18.3P
            length=1,
            default="0",
            validation=CNABFieldType.Int,  # originalmente no manual esta alfa mas foi mudado para int para funcionar
            required=True,
        ),
        "seu_numero": CNABField(  # 19.3P   Campo de preenchimento obrigatório; preencher com Seu Número de controle do título
            length=15,
            default=" ",  # este espaço foi colocado para passa a validação para os seters do generico
            validation=CNABFieldType.Alfa,
            required=True,
        ),
        "data_vencimento": CNABField(  # 20.3
            length=8, default="", validation=CNABFieldType.Date, required=True
        ),
        "valor": CNABField(  # 21.3P
            length=13,
            default="0",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "agencia_cobradora": CNABField(  # 22.3P
            length=5, default="0", validation=CNABFieldType.Int, required=True
        ),
        "agencia_cobradora_dv": CNABField(  # 23.3P
            length=1,
            default=" ",
            validation=CNABFieldType.Alfa,  # originalmente no manual esta alfa mas foi mudado para int para funcionar
            required=True,
        ),
        "especie_titulo": CNABField(  # 24.3P
            length=2, default="2", validation=CNABFieldType.Int, required=True
        ),
        "aceite": CNABField(  # 25.3P
            length=1, default="N", validation=CNABFieldType.Alfa, required=True
        ),
        "data_emissao": CNABField(  # 26.3P
            length=8, default="", validation=CNABFieldType.Date, required=True
        ),
        "codigo_juros": CNABField(  # 27.3P
            length=1, default="3", validation=CNABFieldType.Int, required=True
        ),
        "data_juros": CNABField(  # 28.3P
            length=8, default="0", validation=CNABFieldType.Date, required=True
        ),
        "vlr_juros": CNABField(  # 29.3P
            length=13,
            default="0",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "codigo_desconto": CNABField(  # 30.3P
            length=1, default="0", validation=CNABFieldType.Int, required=True
        ),
        "data_desconto": CNABField(  # 31.3P
            length=8, default="0", validation=CNABFieldType.Date, required=True
        ),
        "vlr_desconto": CNABField(  # 32.3P
            length=13,
            default="0",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "vlr_IOF": CNABField(  # 33.3P
            length=13,
            default="0",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "vlr_abatimento": CNABField(  # 34.3P
            length=13,
            default="0",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "seu_numero2": CNABField(  # 35.3P
            length=25, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "protestar": CNABField(  # 36.3P
            length=1, default="3", validation=CNABFieldType.Alfa, required=True
        ),
        "prazo_protesto": CNABField(  # 37.3P
            length=2, default="0", validation=CNABFieldType.Int, required=True
        ),
        "baixar": CNABField(  # 38.3P
            length=1, default="0", validation=CNABFieldType.Int, required=True
        ),
        "prazo_baixar": CNABField(  # 39.3P
            length=3, default="0", validation=CNABFieldType.Int, required=True
        ),
        "codigo_moeda": CNABField(  # 40.3P
            length=2, default="9", validation=CNABFieldType.Int, required=True
        ),
        "filler4": CNABField(  # 41.3P
            length=10, default="0", validation=CNABFieldType.Int, required=True
        ),
        "filler5": CNABField(  # 42.3P
            length=1, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
    }

    def _inserir_desconto_mensagem(self, **kwargs):
        desconto2 = kwargs.get("codigo_desconto2")
        desconto3 = kwargs.get("codigo_desconto3")
        mensagem = kwargs.get("mensagem")
        if not desconto2 and not desconto3 and not mensagem:
            return
        
        BancoBrasil240Registro3R(self.header, self, self.lote, **kwargs)

    def _inserir_detalhe(self, **kwargs: dict):
        BancoBrasil240Registro3Q(self.header, self, self.lote, **kwargs)
        self._inserir_desconto_mensagem(**kwargs)

        if int(kwargs.get("emissao_boleto")) != 1:
            return
        
        if kwargs.get('mensagem_frente'):
            kwargs['mensagem_140'] = kwargs.get('mensagem_frente')
            kwargs['tipo_impressao'] = 1
            BancoBrasil240Registro3S1e2(self.header, self, self.lote, **kwargs)

        if kwargs.get('mensagem_verso'):
            kwargs['mensagem_140'] = kwargs.get('mensagem_verso')
            kwargs['tipo_impressao'] = 2
            BancoBrasil240Registro3S1e2(self.header, self, self.lote, **kwargs)

        if not kwargs.get('mensagem_5') and not kwargs.get('mensagem_6') and not kwargs.get('mensagem_7') and not kwargs.get('mensagem_8'):
            return
        BancoBrasil240Registro3S3(self.header, self, self.lote, **kwargs)

    def __init__(
        self,
        header: Optional[BancoBrasil240Registro0],
        parent: Optional[Registro],
        lote: BancoBrasil240Registro1,
        **kwargs: dict,
    ):
        super().__init__(header, parent, lote, **kwargs)

        self._inserir_detalhe(**kwargs)
