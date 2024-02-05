from typing import Optional
from datetime import datetime
from cnab.base.registro_remessa import RegistroRemessa
from cnab.base.registro import Registro
from cnab.core.enums import TipoServico, TipoInscricao
from cnab.core.exceptions import CNABInvalidTypeError

class CNAB240Registro1(RegistroRemessa):
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

    def get_tipo_servico(self):
        return self.get_data_or_parent('tipo_servico')
    
    def get_tipo_inscricao(self):
        return self.get_data_or_parent('tipo_inscricao')
    
    def get_numero_inscricao(self):
        return self.get_data_or_parent('numero_inscricao')
    
    def get_agencia(self):
        return self.get_data_or_parent('agencia')
    
    def get_agencia_dv(self):
        return self.get_data_or_parent('agencia_dv')
    
    def get_conta(self):
        return self.get_data_or_parent('conta')
    
    def get_conta_dv(self):
        return self.get_data_or_parent('conta_dv')
    
    def get_convenio(self):
        return self.get_data_or_parent('convenio')
    
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
    
    def get_text(self) -> str:
        dataReg5 = {}
        dataReg5['qtd_titulos_simples'] = 0
        dataReg5['qtd_titulos_caucionada'] = 0
        dataReg5['qtd_titulos_descontada'] = 0
        dataReg5['vrl_titulos_simples'] = 0.00
        dataReg5['vlr_titulos_caucionada'] = 0.00
        dataReg5['vlr_titulos_descontada'] = 0.00

        retorno = ''
        for key, field in self._meta.items():
            retorno += self.get_value(key, field.default)

        result = [retorno]

        if self._children:
            for child in self._children:
                if child.get_codigo_carteira() == 1:
                    dataReg5['qtd_titulos_simples'] += 1
                    dataReg5['vrl_titulos_simples'] += float(child.get_unformated('valor'))
                if child.get_codigo_carteira() == 3:
                    dataReg5['qtd_titulos_caucionada'] += 1
                    dataReg5['vlr_titulos_caucionada'] += float(child.get_unformated('valor'))
                if child.get_codigo_carteira() == 4:
                    dataReg5['qtd_titulos_descontada'] += 1
                    dataReg5['vlr_titulos_descontada'] += float(child.get_unformated('valor'))
                result += child.get_text()

            if not hasattr(self, 'registro5_class'):
                raise Exception("TODO: change the text of this exception")
            if not self.registro5_class:
                raise Exception("TODO: change the text of this exception")
                
            reg5 = self.registro5_class(None, None, self, **dataReg5)
            result += reg5.get_text()

        return result
    
    def append(self, child: Registro):
        super().append(child)

        self.counter += 1
