from .banco_brasil import __all__ as __all_banco_brasil__
from .bradesco import __all__ as __all_bradesco__
from .caixa import __all__ as __all_caixa__
from .itau import __all__ as __all_itau__
from .santander import __all__ as __all_santander__

__all__ = (
    __all_caixa__
    + __all_itau__
    + __all_bradesco__
    + __all_banco_brasil__
    + __all_santander__
)
