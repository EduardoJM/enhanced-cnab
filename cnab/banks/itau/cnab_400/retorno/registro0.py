from cnab.base.retorno import RegistroRetorno
from cnab.core.field import CNABField, CNABFieldType

class ItauRetornoCnab400Registro0(RegistroRetorno):
    _meta = {
        'tipo_registro': CNABField(
            length=1,
            default='0',
            validation=CNABFieldType.Int,
            required=True
        ),
        'operacao': CNABField(
            length=1,
            default='2',
            validation=CNABFieldType.Int,
            required=True
        ),
        'literal_remessa': CNABField(
            length=7,
            default='RETORNO',
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
        'nome_empresa': CNABField(
            length=30,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'codigo_banco': CNABField(
            length=3,
            default='341',
            validation=CNABFieldType.Int,
            required=True),
        'nome_banco': CNABField(
            length=15,
            default='BANCO ITAU SA',
            validation=CNABFieldType.Alfa,
            required=True),
        'data_gravacao': CNABField(
            length=6,
            default='',
            validation=CNABFieldType.Date,
            required=True),
        'filler3': CNABField(
            length=294,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'numero_sequencial_arquivo': CNABField(
            length=6,
            default='',
            validation=CNABFieldType.Int,
            required=True),
    }
