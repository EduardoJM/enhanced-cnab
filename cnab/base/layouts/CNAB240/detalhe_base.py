from typing import Optional
from cnab.base.registro_remessa import RegistroRemessa
from cnab.base.registro_base import RegistroBase
from .lote_base import CNAB240LoteBase

class CNAB240DetalheBase(RegistroRemessa):
    lote: CNAB240LoteBase = None

    def __init__(self,
        header: Optional["RegistroBase"],
        parent: Optional["RegistroBase"],
        lote: CNAB240LoteBase,
        **kwargs: dict,
    ):
        self.lote = lote
        super().__init__(header, parent, **kwargs)
        self.init_numero_registro()

    def init_numero_registro(self):
        self._data['numero_registro'] = self.lote.counter
        #return self.lote.counter

    def get_agencia(self):
        return self.get_data_or_parent('agencia')
    
    def get_agencia_dv(self):
        return self.get_data_or_parent('agencia_dv')
    
    def get_conta(self):
        return self.get_data_or_parent('conta')

    def get_conta_dv(self):
        return self.get_data_or_parent('conta_dv')
    
    def get_codigo_beneficiario(self):
        return self.get_data_or_parent('codigo_beneficiario')

    def get_codigo_beneficiario_dv(self):
        return self.get_data_or_parent('codigo_beneficiario_dv')
    
    def get_cep_pagador(self):
        cep = self.get_data_or_parent('cep_pagador')
        return cep.replace('-', '')
    
    def get_seu_numero2(self):
        value = self._data.get('seu_numero2')
        if value:
            return value
        
        if hasattr(self, 'get_nosso_numero'):
            return self.get_nosso_numero()
        
        return self._data.get('nosso_numero')
    
    def append(self, child: RegistroBase):
        super().append(child)
        self.lote.counter += 1
    