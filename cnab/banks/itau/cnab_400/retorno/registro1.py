from cnab.base.retorno.CNAB400 import Registro1Retorno
from cnab.core.field import CNABField, CNABFieldType

class ItauRetornoCnab400Registro1(Registro1Retorno):
    _meta = {
        'tipo_registro': CNABField(
            length=1,
            default='1',
            validation=CNABFieldType.Int,
            required=True),
        'tipo_inscricao_empresa': CNABField(
            length=2,
            default='',
            validation=CNABFieldType.Int,
            required=True),
        'numero_inscricao_empresa': CNABField(
            length=14,
            default='',
            validation=CNABFieldType.Int,
            required=True),
        'agencia': CNABField(
            length=4,
            default='',
            validation=CNABFieldType.Int,
            required=True),
        'filler1': CNABField(
            length=2,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'conta': CNABField(
            length=5,
            default='',
            validation=CNABFieldType.Int,
            required=True),
        'conta_dv': CNABField(
            length=1,
            default='',
            validation=CNABFieldType.Int,
            required=True),
        'filler2': CNABField(
            length=8,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'seu_numero': CNABField(
            length=25,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'nosso_numero': CNABField(
            length=8,
            default='',
            validation=CNABFieldType.Int,
            required=True),
        'filler3': CNABField(
            length=12,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'carteira': CNABField(      #13.3P
            length=3,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'filler34': CNABField(
            length=9,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'filler4': CNABField(
            length=13,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'cod_carteira': CNABField(      #13.3P
            length=1,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'codigo_movimento': CNABField(      # codigo da ocorrencia no manual itau
            length=2,
            default='01', # entrada de titulo
            validation=CNABFieldType.Int,
            required=True),
        'data_ocorrencia': CNABField(      # codigo da ocorrencia no manual itau
            length=6,
            default='0', # entrada de titulo
            validation=CNABFieldType.Date,
            required=True),
        'seu_numero2': CNABField(            #20.3
            length=10,
            default='',
            validation=CNABFieldType.Alfa,
            required=True),
        'filler41': CNABField(            #20.3
            length=8,
            default='',
            validation=CNABFieldType.Alfa,
            required=True),
        'filler42': CNABField(            #20.3
            length=12,
            default='',
            validation=CNABFieldType.Alfa,
            required=True),
        'data_vencimento': CNABField(            #26.3P
            length=6,
            default='',
            validation=CNABFieldType.Date,
            required=True),
        'valor': CNABField(                 #21.3P
            length=11,
            default='',
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True),
        'codigo_banco': CNABField(
            length=3,
            default='341',
            validation=CNABFieldType.Int,
            required=True),
        'agencia_cobradora': CNABField(    #22.3P
            length=4,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'agencia_cobradora_dv': CNABField(    #22.3P
            length=1,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'especie_titulo': CNABField(    #24.3P
            length=2,
            default='2',
            validation=CNABFieldType.Int,
            required=True),
        'vlr_tarifas': CNABField(            #25.3P
            length=11,
            default='',
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True),
        'filler43': CNABField(            #20.3
            length=26,
            default='',
            validation=CNABFieldType.Alfa,
            required=True),
        'vlr_iof': CNABField(               # 11.3Q
            length=11,
            default='',
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True),
        'vlr_abatimento': CNABField(       #10.3Q
            length=11,
            default='',
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True),
        'vlr_desconto': CNABField(            # 9.3Q
            length=11,
            default='',
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True),
        'vlr_pago': CNABField(               #12.3Q
            length=11,
            default='',
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True),
        'vlr_juros_multa': CNABField(               # 8.3Q
            length=11,
            default='',
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True),
        'vlr_outros': CNABField(               # 8.3Q
            length=11,
            default='',
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True),
        'boleto_dda': CNABField(            #26.3P
            length=1,
            default='',
            validation=CNABFieldType.Alfa,
            required=True),
        'filler44': CNABField(    #24.3P
            length=2,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'data_credito': CNABField(            #26.3P
            length=6,
            default='',
            validation=CNABFieldType.Date,
            required=True),
        'cod_instrucao_cancelada': CNABField(    #24.3P
            length=4,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'filler45': CNABField(    #24.3P
            length=6,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'filler46': CNABField(            #29.3P
            length=13,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'nome_pagador': CNABField(       #10.3Q
            length=30,
            default='',
            validation=CNABFieldType.Alfa,
            required=True),
        'filler47': CNABField(
            length=23,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'erros_mensagens': CNABField(               # 11.3Q
            length=8,
            default='',
            validation=CNABFieldType.Alfa,
            required=True),
        'filler5': CNABField(               #12.3Q
            length=7,
            default='',
            validation=CNABFieldType.Alfa,
            required=True),
        'cod_liquidacao': CNABField(      #13.3Q   
            length=2,
            default='',
            validation=CNABFieldType.Alfa,
            required=True),
        'numero_registro': CNABField(       # 4.3R
            length=6,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
    }
