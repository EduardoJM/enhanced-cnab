from typing import Optional, Union
from cnab.base.cnab_400 import CNAB400Registro1
from cnab.core.field import CNABField, CNABFieldType
from cnab.utils.dict_utils import set_if_has_value
from cnab.base.registro import Registro


class BradescoCnab400Registro1(CNAB400Registro1):
    _meta = {
        'tipo_registro': CNABField(
            length=1,
            default='1',
            validation=CNABFieldType.Int,
            required=True),
        'agencia_debito': CNABField(
            length=5,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'digito_agencia_debito': CNABField(
            length=1,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'razao_conta_corrente_pagador': CNABField(
            length=5,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'conta_corrente_pagador': CNABField(
            length=7,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'digito_conta_corrente_pagador': CNABField(
            length=1,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'filler0': CNABField(
            length=1,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'carteira_banco': CNABField(
            length=3,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'agencia': CNABField(
            length=5,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'conta': CNABField(
            length=7,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'conta_dv': CNABField(
            length=1,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'seu_numero': CNABField(
            length=25,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'codigo_banco_debito': CNABField(
            length=3,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'codigo_multa': CNABField(
            length=1,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'taxa_multa': CNABField(
            length=2,
            default='0',
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True),
        'nosso_numero': CNABField(
            length=11,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'nosso_numero_dv': CNABField(
            length=1,
            default='0',
            validation=CNABFieldType.Alfa,
            required=True),
        'vlr_bonificacao_dia': CNABField(
            length=8,
            default='0',
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True),
        'emissao_boleto': CNABField(
            length=1,
            default='2',
            validation=CNABFieldType.Int,
            required=True),
        'debito_automatico': CNABField(
            length=1,
            default='N',
            validation=CNABFieldType.Alfa,
            required=True),
        'filler6': CNABField(
            length=10,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'indicador_rateio': CNABField(
            length=1,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'endereco_aviso_debito': CNABField(# 2 = ignora
            length=1,
            default='2',
            validation=CNABFieldType.Int,
            required=True),
        'filler7': CNABField(
            length=2,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'codigo_movimento': CNABField(
            length=2,
            default=1,
            validation=CNABFieldType.Int,
            required=True),
        'numero_documento': CNABField(
            length=10,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'data_vencimento': CNABField(
            length=6,
            default='',
            validation=CNABFieldType.Date,
            required=True),
        'valor': CNABField(
            length=11,
            default='',
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True),
        'banco_cobrador': CNABField(
            length=3,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'agencia_cobradora': CNABField(
            length=5,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'especie_titulo': CNABField(
            length=2,
            default='1',
            validation=CNABFieldType.Int,
            required=True),
        'aceite': CNABField(
            length=1,
            default='N',
            validation=CNABFieldType.Alfa,
            required=True),
        'data_emissao': CNABField(
            length=6,
            default='',
            validation=CNABFieldType.Date,
            required=True),
        'cod_instrucao1': CNABField(
            length=2,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'cod_instrucao2': CNABField(
            length=2,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'vlr_juros': CNABField(
            length=11,
            default='0',
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True),
        'data_desconto': CNABField(
            length=6,
            default='0',
            validation=CNABFieldType.Date,
            required=True),
        'vlr_desconto': CNABField(
            length=11,
            default='0',
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True),
        'vlr_IOF': CNABField(
            length=11,
            default='0',
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True),
        'vlr_abatimento': CNABField(
            length=11,
            default='0',
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True),
        'tipo_inscricao': CNABField(
            length=2,
            default='',
            validation=CNABFieldType.Int,
            required=True),
        'numero_inscricao': CNABField(
            length=14,
            default='',
            validation=CNABFieldType.Int,
            required=True),
        'nome_pagador': CNABField(
            length=40,
            default='',
            validation=CNABFieldType.Alfa,
            required=True),
        'endereco_pagador': CNABField(
            length=40,
            default='',
            validation=CNABFieldType.Alfa,
            required=True),
        '1_mensagem': CNABField(
            length=12,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'cep_pagador': CNABField(
            length=8,
            default='',
            validation=CNABFieldType.Int,
            required=True),
        '2_mensagem': CNABField(
            length=60,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'numero_registro': CNABField(
            length=6,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
    }

    def __init__(self, header: Registro | None, parent: Registro | None, **kwargs: dict):
        super().__init__(header, parent, **kwargs)

    def inserir_mensagem(self, **kwargs):
        if not kwargs.get('mensagem'):
            return
        from .registro2 import BradescoCnab400Registro2
        return BradescoCnab400Registro2(self.header, self, kwargs)
