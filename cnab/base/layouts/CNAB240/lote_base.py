from typing import Optional
from datetime import datetime
from cnab.base.registro_remessa import RegistroRemessa
from cnab.base.registro_base import RegistroBase
from cnab.core.enums import TipoServico, TipoInscricao
from cnab.core.exceptions import CNABInvalidTypeError

class CNAB240LoteBase(RegistroRemessa):
    def __init__(self, parent: Optional["RegistroBase"],**kwargs: dict):
        self.counter = 0
        super().__init__(parent, **kwargs)

    def set_codigo_lote(self):
        self._data['codigo_lote'] = self.counter

    def set_tipo_servico(self, value: TipoServico):
        if not isinstance(value, TipoServico):
            raise CNABInvalidTypeError(TipoServico)

        self._data['tipo_servico'] = value.value

    def set_tipo_inscricao(self, value: TipoInscricao):
        if not isinstance(value, TipoInscricao):
            raise CNABInvalidTypeError(TipoInscricao)
        
        self._data['tipo_inscricao'] = value.value

    def get_data_or_parent(self, field: str):
        if self._data.get(field):
            return self._data.get(field)
        if not self.parent:
            return None
        return self.parent.get_value(field, None)

    def get_tipo_servico(self):
        return self.get_data_or_parent('tipo_servico')
    
    def get_tipo_inscricao(self):
        return self.get_data_or_parent('tipo_inscricao')
    
    def get_numero_inscricao(self):
        return self.get_data_or_parent('numero_inscricao')
    
    def get_agencia(self):
        return self.get_data_or_parent('agencia')
    
    def get_nome_empresa(self):
        return self.get_data_or_parent('nome_empresa')
    
    def get_numero_remessa(self):
        return self.get_data_or_parent('numero_sequencial_arquivo')
    
    def get_data_gravacao(self):
        return datetime.now()

    def get_codigo_beneficiario(self):
        return self.get_data_or_parent('codigo_beneficiario')
    
    def get_codigo_beneficiario_dv(self):
        return self.get_data_or_parent('codigo_beneficiario_dv')
