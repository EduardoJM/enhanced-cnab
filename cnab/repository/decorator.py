from .layouts_repository import LayoutsRepository

def register_retorno_layout(bank_code: str, layout_code: str):
    def wrapper(cls):
        LayoutsRepository.register_retorno(bank_code, layout_code, cls)
        return cls
    return wrapper

def register_remessa_layout(bank_code: str, layout_code: str):
    def wrapper(cls):
        LayoutsRepository.register_remessa(bank_code, layout_code, cls)
        return cls
    return wrapper
