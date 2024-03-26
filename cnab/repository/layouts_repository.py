from typing import Dict
from cnab.base.remessa import Remessa
from cnab.base.retorno import Retorno

def _get_layout_name(bank_code: str, layout_code: str):
    return f"B_{bank_code}_{layout_code}"

class LayoutsRepository:
    RETORNOS: Dict[str, type[Retorno]] = {}
    REMESSAS: Dict[str, type[Remessa]] = {}

    @classmethod
    def register_retorno(cls, bank_code: str, layout_code: str, retorno_class: type[Retorno]):
        code = _get_layout_name(bank_code, layout_code)
        cls.RETORNOS[code] = retorno_class
    
    @classmethod
    def register_remessa(cls, bank_code: str, layout_code: str, remessa_class: type[Remessa]):
        code = _get_layout_name(bank_code, layout_code)
        cls.RETORNOS[code] = remessa_class

    @classmethod
    def get_retorno_class(cls, bank_code: str, layout_code: str):
        code = _get_layout_name(bank_code, layout_code)
        return cls.RETORNOS.get(code)
    
    @classmethod
    def get_remessa_class(cls, bank_code: str, layout_code: str):
        code = _get_layout_name(bank_code, layout_code)
        return cls.REMESSAS.get(code)
