from typing import Optional
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
            #field.registro = self
            #default = self.get_default(field)
            retorno += field.get_value()

        result = [retorno]

        if self._children:
            for child in self._children:
                if child.get_codigo_carteira() == 1:
                    dataReg5['qtd_titulos_simples'] += 1
                    dataReg5['vrl_titulos_simples'] += float(child.valor)
                if child.get_codigo_carteira() == 3:
                    dataReg5['qtd_titulos_caucionada'] += 1
                    dataReg5['vlr_titulos_caucionada'] += float(child.valor)
                if child.get_codigo_carteira() == 4:
                    dataReg5['qtd_titulos_descontada'] += 1
                    dataReg5['vlr_titulos_descontada'] += float(child.valor)
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
