from typing import Optional
from cnab.base.cnab_240 import CNAB240Registro3
from cnab.core.field import CNABField, CNABFieldType
from cnab.base.registro import Registro
from cnab.utils.check_digit import compute_check_digit
from .registro3Q import Santander240Registro3Q
from .registro1 import Santander240Registro1
from .registro3R import Santander240Registro3R

class Santander240Registro3P(CNAB240Registro3):
    _meta = {
        "codigo_banco": CNABField(
            length=3, default="033", validation=CNABFieldType.Int, required=True
        ),
        "codigo_lote": CNABField(
            length=4, default=1, validation=CNABFieldType.Int, required=True
        ),
        "tipo_registro": CNABField(
            length=1, default="3", validation=CNABFieldType.Int, required=True
        ),
        "numero_registro": CNABField(
            length=5, default="0", validation=CNABFieldType.Int, required=True
        ),
        "seguimento": CNABField(
            length=1, default="P", validation=CNABFieldType.Alfa, required=True
        ),
        "filler1": CNABField(
            length=1, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "codigo_movimento": CNABField(
            length=2,
            default="01",  # entrada de titulo
            validation=CNABFieldType.Int,
            required=True,
        ),
        # - ------------------ até aqui é igual para todo registro tipo 3
        "agencia": CNABField(
            length=4, default="", validation=CNABFieldType.Int, required=True
        ),
        "agencia_dv": CNABField(
            length=1, default="", validation=CNABFieldType.Int, required=True
        ),
        "conta": CNABField(
            length=9, default="0", validation=CNABFieldType.Int, required=True
        ),
        "conta_dv": CNABField(
            length=1, default="", validation=CNABFieldType.Int, required=True
        ),
        "codigo_beneficiario": CNABField(
            length=9, default="", validation=CNABFieldType.Int, required=True
        ),
        "codigo_beneficiario_dv": CNABField(
            length=1, default="", validation=CNABFieldType.Int, required=True
        ),
        "filler2": CNABField(
            length=2, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "nosso_numero": CNABField(
            length=13, default="", validation=CNABFieldType.Int, required=True
        ),
        "tipo_cobranca": CNABField(
            length=1, default="5", validation=CNABFieldType.Int, required=True
        ),
        "forma_cadastramento": CNABField(
            length=1,
            default="1",  # '1' = Cobrança Registrada (Rápida e Eletrônica com Registro)
            validation=CNABFieldType.Int,
            required=True,
        ),
        "tipo_documento": CNABField(
            length=1,
            default="1",  # 1- Tradicional , 2- Escritural
            validation=CNABFieldType.Int,
            required=True,
        ),
        "filler3": CNABField(
            length=1, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "filler4": CNABField(
            length=1, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "seu_numero": CNABField(
            length=15, default="", validation=CNABFieldType.Int, required=True
        ),
        "data_vencimento": CNABField(
            length=8, default="", validation=CNABFieldType.Date, required=True
        ),
        "valor": CNABField(
            length=13,
            default="",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "agencia_cobradora": CNABField(
            length=4, default="0", validation=CNABFieldType.Int, required=True
        ),
        "agencia_cobradora_dv": CNABField(
            length=1, default="0", validation=CNABFieldType.Int, required=True
        ),
        "filler5": CNABField(
            length=1, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "especie_titulo": CNABField(
            length=2, default="2", validation=CNABFieldType.Int, required=True
        ),
        "aceite": CNABField(
            length=1, default="N", validation=CNABFieldType.Alfa, required=True
        ),
        "data_emissao": CNABField(
            length=8, default="", validation=CNABFieldType.Date, required=True
        ),
        #
        # Códigos dos juros de mora
        # 1 = Valor por dia - Informar no campo o valor/dia a mora a ser cobrada.
        # 2 = Taxa Mensal - Informar no campo taxa mensal o percentual a ser aplicado sobre valor do titulo que será calculado por dia de atraso.
        # 3 = Isento
        # 4 = Utilizar comissão permanência do Banco por dia de atraso
        # 5 = Tolerância valor por dia (cobrar juros a partir de)
        # 6 = Tolerância taxa mensal (cobrar juros a partir de)
        # Para o código igual 4, o campo “taxa mensal” não deverá conter informação.
        #
        "codigo_juros": CNABField(
            length=1, default="0", validation=CNABFieldType.Int, required=True
        ),
        "data_juros": CNABField(
            length=8, default="0", validation=CNABFieldType.Date, required=True
        ),
        "vlr_juros": CNABField(
            length=13,
            default="0",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        #
        # 0 = ISENTO
        # 1 = Valor fixo ate a data informada – Informar o valor no campo “valor de desconto a ser concedido”.
        # 2 = Percentual ate a data informada – Informar o percentual no campo “percentual de desconto a ser concedido”
        # 3 = Valor por antecipação por dia corrido - Informar o valor no campo “valor de desconto a ser concedido”
        # 4 = Valor por antecipação dia útil - Informar o valor no campo “valor de desconto a ser concedido” Para os código 1 e 2 será obrigatório a informação da “data” NOTA: é possível informar até duas ocorrências de desconto, por ex.:
        #      Segmento P : Valor do titulo R$ 100,00 Vencimento 30/09/1998
        #      ( Desconto 1 R$ 10,00 p/ pagamento até 25/09/1998
        #      Segmento R: < Desconto 2 R$ 8,00 p/ pagamento até 20/09/1998
        #
        "codigo_desconto": CNABField(
            length=1, default="0", validation=CNABFieldType.Int, required=True
        ),
        "data_desconto": CNABField(
            length=8, default="0", validation=CNABFieldType.Date, required=True
        ),
        "vlr_desconto": CNABField(
            length=13,
            default="0",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "vlr_IOF": CNABField(
            length=13,
            default="0",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "vlr_abatimento": CNABField(
            length=13,
            default="0",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "seu_numero2": CNABField(
            length=25, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        #
        # 0 NAO PROTESTAR
        # 1 PROTESTAR DIAS CORRIDOS
        # 2 PROTESTAR DIAS UTEIS
        # 3 UTILIZAR PERFIL BENEFICIÁRIO
        # 9 CANCELAMENTO DE PROTESTO AUTOMATICO
        #
        "protestar": CNABField(
            length=1, default=3, validation=CNABFieldType.Alfa, required=True
        ),
        "prazo_protesto": CNABField(
            length=2, default="0", validation=CNABFieldType.Int, required=True
        ),
        #
        # 1 BAIXAR / DEVOLVER
        # 2 NAO BAIXAR / NAO DEVOLVER
        # 3 UTILIZAR PERFIL BENEFICIÁRIO
        #
        "baixar": CNABField(
            length=1, default="1", validation=CNABFieldType.Int, required=True
        ),
        "filler6": CNABField(
            length=1, default="0", validation=CNABFieldType.Int, required=True
        ),
        "prazo_baixar": CNABField(
            length=2, default="90", validation=CNABFieldType.Int, required=True
        ),
        "codigo_moeda": CNABField(
            length=2, default="00", validation=CNABFieldType.Int, required=True
        ),
        "filler7": CNABField(
            length=11, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
    }

    def _inserir_detalhe(self, **kwargs: dict):
        if int(kwargs.get('codigo_movimento')) == 2:
            return
        
        Santander240Registro3Q(self.header, self, self.lote, **kwargs)
        
        desconto2 = kwargs.get('codigo_desconto2')
        desconto3 = kwargs.get('codigo_desconto3')
        vlr_multa = kwargs.get('vlr_multa')
        informacao_pagador = kwargs.get('informacao_pagador')
        if not desconto2 and not desconto3 and not vlr_multa and not informacao_pagador:
            return
        
        Santander240Registro3R(self.header, self, self.lote, **kwargs)

    def __init__(
        self,
        header: Optional["Registro"],
        parent: Optional["Registro"],
        lote: Santander240Registro1,
        **kwargs: dict
    ):
        super().__init__(header, parent, lote, **kwargs)

        self._inserir_detalhe(**kwargs)

    def get_codigo_beneficiario(self):
        return self.get_data_or_parent('conta')
    
    def get_codigo_beneficiario_dv(self):
        return self.get_data_or_parent('conta_dv')
    
    def get_nosso_numero(self):
        num = str(self._data.get('nosso_numero'))
        if num == "0" or num == " ":
            return num
        return num + str(compute_check_digit(num))

