from typing import Optional, Union, TYPE_CHECKING
from cnab.base.remessa import Remessa
from cnab.utils.dict_utils import set_if_has_value
from .registro0 import BancoBrasil240Registro0
from .registro9 import BancoBrasil240Registro9

if TYPE_CHECKING:
    from .registro1 import BancoBrasil240Registro1

class CNAB240BancoBrasil(Remessa):
    header: BancoBrasil240Registro0
    registro0_class = BancoBrasil240Registro0
    registro9_class = BancoBrasil240Registro9

    def __init__(
        self,
        *,
        codigo_lote: Optional[Union[str, int]] = None,
        tipo_registro: Optional[Union[str, int]] = None,
        tipo_inscricao: Optional[Union[str, int]] = None,
        numero_inscricao: Optional[Union[str, int]] = None,
        convenio: Optional[Union[str, int]] = None,
        cobranca_cedente: Optional[Union[str, int]] = None,
        carteira_cobranca: Optional[Union[str, int]] = None,
        variacao_carteira_cobranca: Optional[Union[str, int]] = None,
        agencia: Optional[Union[str, int]] = None,
        agencia_dv: Optional[Union[str, int]] = None,
        conta: Optional[Union[str, int]] = None,
        conta_dv: Optional[Union[str, int]] = None,
        nome_empresa: Optional[str] = None,
        codigo_remessa: Optional[Union[str, int]] = None,
        numero_sequencial_arquivo: Optional[Union[str, int]] = None,
        **kwargs,
    ):
        set_if_has_value(kwargs, 'codigo_lote', codigo_lote)
        set_if_has_value(kwargs, 'tipo_registro', tipo_registro)
        set_if_has_value(kwargs, 'tipo_inscricao', tipo_inscricao)
        set_if_has_value(kwargs, 'numero_inscricao', numero_inscricao)
        set_if_has_value(kwargs, 'convenio', convenio)
        set_if_has_value(kwargs, 'cobranca_cedente', cobranca_cedente)
        set_if_has_value(kwargs, 'carteira_cobranca', carteira_cobranca)
        set_if_has_value(kwargs, 'variacao_carteira_cobranca', variacao_carteira_cobranca)
        set_if_has_value(kwargs, 'agencia', agencia)
        set_if_has_value(kwargs, 'agencia_dv', agencia_dv)
        set_if_has_value(kwargs, 'conta', conta)
        set_if_has_value(kwargs, 'conta_dv', conta_dv)
        set_if_has_value(kwargs, 'nome_empresa', nome_empresa)
        set_if_has_value(kwargs, 'codigo_remessa', codigo_remessa)
        set_if_has_value(kwargs, 'numero_sequencial_arquivo', numero_sequencial_arquivo)
        super().__init__(**kwargs)

    def inserir_lote(
        self,
        *,
        tipo_servico: Optional[Union[str, int]] = None,
        variacao: Optional[Union[str, int]] = None,
        **kwargs,
    ) -> "BancoBrasil240Registro1":
        set_if_has_value(kwargs, 'tipo_servico', tipo_servico)
        set_if_has_value(kwargs, 'variacao', variacao)
        return super().inserir_lote(**kwargs)
