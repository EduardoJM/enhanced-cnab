from abc import abstractmethod
from enum import Enum
from typing import Union
from cnab.core.exceptions import CNABInvalidEspecieTituloError
from .banks import BANKS

class EspecieTitulo(Enum):
    Cheque = 'CH'
    DuplicataMercantil = 'DM'
    MercantilParaIndicacao = 'DMI'
    DuplicataDeServico = 'DS'
    DuplicataDeServicoParaIndicacao = 'DSI'
    DuplicataRural = 'DR'
    LetraCambio = 'LC'
    NotaCreditoComercial = 'NCC'
    NotaCreditoExportacao = 'NCE'
    NotaCreditoExportacaoIndicacao = 'NCI'
    NotaCreditoRural = 'NCR'
    NotaPromissoria = 'NP'
    NotaPromissoriaRural = 'NPR'
    TriplicataMercantil = 'TM'
    TriplicataServico = 'TS'
    NotaSeguro = 'NS'
    Recibo = 'RC'
    Fatura = 'FAT'
    NotaDebito = 'ND'
    Warrant = 'WRT'
    ApoliceSeguros = 'AP'
    MensalidadeEscolar = 'ME'
    ParcelaConsorcio = 'ME'
    Contrato = 'CT'
    Cosseguros = 'CS'
    DocumentoDivida = 'DV'
    EncargosCondominiais = 'EC'
    ContaPrestacaoServicoes = 'CPS'
    BoletoProposta = 'DBP'
    CartaoCredito = 'CC'
    Outros = 'DIV'

    @abstractmethod
    def get_real_value(bank: Union[str, int], value: Union[str, "EspecieTitulo"]):
        default_value = value
        if isinstance(value, EspecieTitulo):
            value = value.value
        
        if not BANKS.get(str(bank)):
            raise CNABInvalidEspecieTituloError(default_value, bank)
        codes = BANKS.get(str(bank)).values()
        if value in codes:
            return value
        code = BANKS.get(str(bank)).get(value)
        if not code:
            raise CNABInvalidEspecieTituloError(default_value, bank)
        return code
    
__all__ = ['EspecieTitulo']
