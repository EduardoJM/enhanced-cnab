from typing import Optional, Union, TYPE_CHECKING
from cnab.base.remessa.CNAB240 import CNAB240Registro1
from cnab.core.field import (
    CNABFieldInteger,
    CNABFieldAlfa,
    CNABCreatedDateField
)
from cnab.utils.dict_utils import set_if_has_value
from .registro5 import BancoBrasil240Registro5

if TYPE_CHECKING:
    from .registro0 import BancoBrasil240Registro0

class BancoBrasil240Registro1(CNAB240Registro1):
    registro5_class = BancoBrasil240Registro5
    
    codigo_banco = CNABFieldInteger("",length=3, default="001", required=True)
    codigo_lote = CNABFieldInteger("",length=4, default=1, required=True)
    tipo_registro = CNABFieldInteger("",length=1, default=1, required=True)
    operacao = CNABFieldAlfa("",length=1, default="R", required=True)
    tipo_servico = CNABFieldInteger("",length=2, default="01", required=True)
    filler1 = CNABFieldAlfa("",length=2, default=" ", required=True)
    versa_layout = CNABFieldInteger("",length=3, default="000", required=True)
    filler2 = CNABFieldAlfa("",length=1, default=" ", required=True)
    tipo_inscricao = CNABFieldInteger("",length=1, default="0", required=True)
    numero_inscricao = CNABFieldInteger("",length=15, default="", required=True)
    convenio = CNABFieldInteger("",length=9, default="0", required=True)
    cobranca = CNABFieldInteger("",length=4, default="0014", required=True)
    carteira = CNABFieldInteger("",length=2, default="0", required=True)
    variacao = CNABFieldInteger("",length=3, default="000", required=True)
    situacao_arquivo = CNABFieldAlfa("",length=2, default=" ", required=True)
    agencia = CNABFieldInteger("",length=5, default="", required=True)
    agencia_dv = CNABFieldAlfa("",length=1, default="", required=True)
    conta = CNABFieldInteger("",length=12, default="", required=True)
    conta_dv = CNABFieldAlfa("",length=1, default="", required=True)
    filler3 = CNABFieldAlfa("",length=1, default="0", required=True)
    nome_empresa = CNABFieldAlfa("",length=30, default="", required=True)
    mensagem_fixa1 = CNABFieldAlfa("",length=40, default=" ", required=True)
    mensagem_fixa2 = CNABFieldAlfa("",length=40, default=" ", required=True)
    numero_remessa = CNABFieldInteger("",length=8, default="0", required=True,value_from='numero_sequencial_arquivo')
    data_gravacao = CNABCreatedDateField("",length=8,required=True,)
    filler4 = CNABFieldInteger("",length=8, default="0", required=True)
    filler5 = CNABFieldAlfa("",length=33, default=" ", required=True)


    def __init__(
        self,
        header: "BancoBrasil240Registro0",
        parent: "BancoBrasil240Registro0",
        *,
        codigo_banco: Optional[Union[str, int]] = None,
        codigo_lote: Optional[Union[str, int]] = None,
        tipo_registro: Optional[Union[str, int]] = None,
        operacao: Optional[Union[str, int]] = None,
        tipo_servico: Optional[Union[str, int]] = None,
        tipo_inscricao: Optional[Union[str, int]] = None,
        numero_inscricao: Optional[Union[str, int]] = None,
        convenio: Optional[Union[str, int]] = None,
        cobranca: Optional[Union[str, int]] = None,
        carteira: Optional[Union[str, int]] = None,
        variacao: Optional[Union[str, int]] = None,
        agencia: Optional[Union[str, int]] = None,
        agencia_dv: Optional[Union[str, int]] = None,
        conta: Optional[Union[str, int]] = None,
        conta_dv: Optional[Union[str, int]] = None,
        nome_empresa: Optional[str] = None,
        mensagem_fixa1: Optional[str] = None,
        mensagem_fixa2: Optional[str] = None,
        numero_remessa: Optional[Union[str, int]] = None,
        **kwargs: dict,):
        set_if_has_value(kwargs, 'codigo_banco', codigo_banco)
        set_if_has_value(kwargs, 'codigo_lote', codigo_lote)
        set_if_has_value(kwargs, 'tipo_registro', tipo_registro)
        set_if_has_value(kwargs, 'operacao', operacao)
        set_if_has_value(kwargs, 'tipo_servico', tipo_servico)
        set_if_has_value(kwargs, 'tipo_inscricao', tipo_inscricao)
        set_if_has_value(kwargs, 'numero_inscricao', numero_inscricao)
        set_if_has_value(kwargs, 'convenio', convenio)
        set_if_has_value(kwargs, 'cobranca', cobranca)
        set_if_has_value(kwargs, 'carteira', carteira)
        set_if_has_value(kwargs, 'variacao', variacao)
        set_if_has_value(kwargs, 'agencia', agencia)
        set_if_has_value(kwargs, 'agencia_dv', agencia_dv)
        set_if_has_value(kwargs, 'conta', conta)
        set_if_has_value(kwargs, 'conta_dv', conta_dv)
        set_if_has_value(kwargs, 'nome_empresa', nome_empresa)
        set_if_has_value(kwargs, 'mensagem_fixa1', mensagem_fixa1)
        set_if_has_value(kwargs, 'mensagem_fixa2', mensagem_fixa2)
        set_if_has_value(kwargs, 'numero_remessa', numero_remessa)
        super().__init__(header, parent, **kwargs)

    def inserir_detalhe(self, **kwargs):
        from .registro3P import BancoBrasil240Registro3P
        return BancoBrasil240Registro3P(self.header, self, self, **kwargs)
