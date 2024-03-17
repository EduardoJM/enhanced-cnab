from typing import Optional, Union
from cnab.base.cnab_400 import CNAB400Registro0
from cnab.core.field import CNABField, CNABFieldType
from cnab.utils.dict_utils import set_if_has_value


class BradescoCnab400Registro0(CNAB400Registro0):
    _meta = {
        'identificacao_registro': CNABField(
            length=1,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'operacao': CNABField(
            length=1,
            default='1',
            validation=CNABFieldType.Int,
            required=True),
        'literal_remessa': CNABField(
            length=7,
            default='remessa',
            validation=CNABFieldType.Alfa,
            required=True),
        'tipo_servico': CNABField(
            length=2,
            default='01',
            validation=CNABFieldType.Int,
            required=True),
        'literal_servico': CNABField(
            length=15,
            default='COBRANCA',
            validation=CNABFieldType.Alfa,
            required=True),
        'codigo_beneficiario': CNABField(
            length=20,
            default='',
            validation=CNABFieldType.Int,
            required=True),
        'nome_empresa': CNABField(
            length=30,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'codigo_banco': CNABField(
            length=3,
            default='237',
            validation=CNABFieldType.Int,
            required=True),
        'nome_banco': CNABField(
            length=15,
            default='Bradesco',
            validation=CNABFieldType.Alfa,
            required=True),
        'data_gravacao': CNABField(
            length=6,
            default='',# nao informar a data na instanciação - gerada dinamicamente
            validation=CNABFieldType.Date,
            required=True),
        'filler1': CNABField(
            length=8,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'identificacao_sistema': CNABField(
            length=2,
            default='MX',
            validation=CNABFieldType.Alfa,
            required=True),
        'numero_sequencial_arquivo': CNABField(
            length=7,
            default='1',
            validation=CNABFieldType.Int,
            required=True),
        'filler2': CNABField(
            length=277,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'numero_sequencial': CNABField(
            length=6,
            default='1',
            validation=CNABFieldType.Int,
            required=True),
    }

    def inserir_detalhe(self, **kwargs):
        from .registro1 import BradescoCnab400Registro1
        return BradescoCnab400Registro1(self, self, **kwargs)
