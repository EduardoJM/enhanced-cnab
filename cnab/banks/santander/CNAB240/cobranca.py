from cnab.base.layouts.CNAB240 import CNAB240DetalheBase
from cnab.core.field import CNABField, CNABFieldType


class Santander240Cobranca(CNAB240DetalheBase):
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
