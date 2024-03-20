from cnab.base.cnab_240 import CNAB240Registro0
from cnab.core.field import (
    CNABField,
    CNABFieldType,
    CNABCreatedDateField,
)
from .registro1 import Caixa240Registro1


class Caixa240Registro0(CNAB240Registro0):
    registro1_class = Caixa240Registro1
    _meta = {
        "codigo_banco": CNABField(  # 01.0
            length=3,
            default="104",
            validation=CNABFieldType.Int,
            required=True
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
            length=1, default="", validation=CNABFieldType.Int, required=True
        ),
        "numero_inscricao": CNABField(  # 06.0
            length=14, default="", validation=CNABFieldType.Int, required=True
        ),
        "filler2": CNABField(  # 07.0
            length=20, default="0", validation=CNABFieldType.Int, required=True
        ),
        "agencia": CNABField(  # 08.0
            length=5, default="", validation=CNABFieldType.Int, required=True
        ),
        "agencia_dv": CNABField(  # 09.0
            length=1, default="", validation=CNABFieldType.Int, required=True
        ),
        "codigo_beneficiario": CNABField( # 10.0
            # TODO: lidar com diferentes layouts
            length=7, default="", validation=CNABFieldType.Int, required=True 
        ),
        "filler3": CNABField(  # 11.0/12.0
            length=7, default="0", validation=CNABFieldType.Int, required=True
        ),
        "nome_empresa": CNABField(  # 13.0
            length=30, default="", validation=CNABFieldType.Alfa, required=True
        ),
        "nome_banco": CNABField(  # 14.0
            length=30, default="CAIXA", validation=CNABFieldType.Alfa, required=True
        ),
        "filler4": CNABField(  # 15.0
            length=10, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "codigo_remessa": CNABField(  # 16.0
            length=1, default="1", validation=CNABFieldType.Int, required=True
        ),
        "data_geracao": CNABCreatedDateField(  # 17.0
            length=8,
            validation=CNABFieldType.Date,
            required=True,
        ),
        "hora_geracao": CNABCreatedDateField(  # 18.00
            length=6,
            validation=CNABFieldType.Time,
            required=True,
        ),
        "numero_sequencial_arquivo": CNABField(  # 19.0
            length=6, default="", validation=CNABFieldType.Int, required=True
        ),
        "versao_layout": CNABField(  # 20.0
            # TODO: lidar com diferentes layouts
            length=3, default="101", validation=CNABFieldType.Int, required=True
        ),
        "densidade_gravacao": CNABField(  # 21.0
            length=5, default="0", validation=CNABFieldType.Int, required=True
        ),
        "filler5": CNABField(  # 22.0
            length=20, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "reservado_empresa": CNABField(  # 23.0
            length=20, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "filler6": CNABField(  # 24.0
            length=4, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "filler7": CNABField(  # 25.0
            length=25, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
    }

    def get_versao_layout(self):
        if self._data.get('versao_layout'):
            return self._data.get('versao_layout')

        codigo_beneficiario = self._data.get('codigo_beneficiario')
        if len(codigo_beneficiario) > 6:
            return '107'
        return '101'
    
    def get_codigo_beneficiario(self):
        codigo_beneficiario = self._data.get('codigo_beneficiario')
        versao_layout = self.get_versao_layout()
        if versao_layout == '101':
            code = str(codigo_beneficiario).rjust(6, '0')
            return f"{code}0"
        if versao_layout == '107':
            return str(codigo_beneficiario).rjust(7, '0')
        # TODO: raise exception here
