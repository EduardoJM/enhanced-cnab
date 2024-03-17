from typing import Optional
from datetime import datetime
from cnab.base.registro_remessa import RegistroRemessa
from cnab.base.registro import Registro
from cnab.core.enums import TipoServico, TipoInscricao
from cnab.core.exceptions import CNABInvalidTypeError
from cnab.core.especie import EspecieTitulo

class CNAB400Registro1(RegistroRemessa):
    def __init__(self, header: Optional["Registro"], parent: Optional["Registro"], **kwargs: dict):
        self.counter = 0
        super().__init__(header, parent, **kwargs)
        self.init_numero_registro()

    def init_numero_registro(self):
        self._data['numero_registro'] = self.header.counter
        self._data['numero_sequencial'] = self.header.counter

    def append(self, child: Registro):
        super().append(child)

        self.counter += 1

    def get_tipo_inscricao_empresa(self):
        return self.get_data_or_parent('tipo_inscricao_empresa')
    
    def get_numero_inscricao_empresa(self):
        return self.get_data_or_parent('numero_inscricao_empresa')
    
    def get_agencia(self):
        return self.get_data_or_parent('agencia')

    def get_conta(self):
        return self.get_data_or_parent('conta')

    def get_conta_dv(self):
        return self.get_data_or_parent('conta_dv')
    
    def get_data_emissao(self):
        return datetime.now()
    
    def get_numero_registro(self):
        return self.get_data_or_parent('numero_sequencial')

    def get_especie_titulo(self):
        field = self.get_field('codigo_banco')
        return EspecieTitulo.get_real_value(
            field.default,
            self._data.get('especie_titulo')
        )
    