from typing import Optional
from datetime import datetime
from cnab.base.registro_remessa import RegistroRemessa
from cnab.base.registro import Registro
from cnab.core.enums import TipoServico, TipoInscricao
from cnab.core.exceptions import CNABInvalidTypeError

class CNAB400Registro1(RegistroRemessa):
    def __init__(self, header: Optional["Registro"], parent: Optional["Registro"], **kwargs: dict):
        self.counter = 0
        super().__init__(header, parent, **kwargs)

    def set_codigo_lote(self):
        self._data['codigo_lote'] = self.header.counter

    def set_tipo_servico(self, value: TipoServico):
        if not isinstance(value, TipoServico):
            raise CNABInvalidTypeError(TipoServico)

        self._data['tipo_servico'] = value.value

    def set_tipo_inscricao(self, value: TipoInscricao):
        if not isinstance(value, TipoInscricao):
            raise CNABInvalidTypeError(TipoInscricao)
        
        self._data['tipo_inscricao'] = value.value

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
    