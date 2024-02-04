from typing import Optional
from cnab.base.layouts.CNAB240 import CNAB240DetalheBase
from cnab.core.field import CNABField, CNABFieldType
from cnab.base.registro_base import RegistroBase

# from cnab.utils.mod11 import calculate_mod11_dv
#from .pagador import Santander240Pagador
from .lote import BancoBrasil240Lote
#from .desconto_multa import Santander240DescontoMulta


class Santander240Cobranca(CNAB240DetalheBase):
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

    def __init__(
        self,
        header: Optional["RegistroBase"],
        parent: Optional["RegistroBase"],
        lote: BancoBrasil240Lote,
        **kwargs: dict,
    ):
        super().__init__(header, parent, lote, **kwargs)

        self.inserir_detalhe(**kwargs)

    def inserir_detalhe(self, **kwargs: dict):
        if int(kwargs.get("codigo_movimento")) == 2:
            return

        """
        TODO: continuar aqui
        Santander240Pagador(self.header, self, self.lote, **kwargs)

        desconto2 = kwargs.get("codigo_desconto2")
        desconto3 = kwargs.get("codigo_desconto3")
        vlr_multa = kwargs.get("vlr_multa")
        informacao_pagador = kwargs.get("informacao_pagador")
        if not desconto2 and not desconto3 and not vlr_multa and not informacao_pagador:
            return

        Santander240DescontoMulta(self.header, self, self.lote, **kwargs)
        """

    """
    def get_codigo_beneficiario(self):
        return self.get_data_or_parent('conta')
    
    def get_codigo_beneficiario_dv(self):
        return self.get_data_or_parent('conta_dv')
    
    def get_nosso_numero(self):
        num = str(self._data.get('nosso_numero'))
        return num + str(calculate_mod11_dv(num))
    """
