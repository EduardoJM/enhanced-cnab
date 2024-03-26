from typing import Optional, Union
from cnab.base.cnab_240 import CNAB240Registro0
from cnab.core.field import (
    CNABFieldInteger,
    CNABFieldAlfa,
    CNABCreatedDateField,
    CNABCreatedTimeField,
)
from cnab.utils.dict_utils import set_if_has_value
from .registro1 import BancoBrasil240Registro1

class BancoBrasil240Registro0(CNAB240Registro0):
    registro1_class = BancoBrasil240Registro1
    
    codigo_banco = CNABFieldInteger("",length=3, default="001", required=True)
    codigo_lote = CNABFieldInteger("",length=4, default="0000", required=True)
    tipo_registro = CNABFieldInteger("",length=1, default="0", required=True)
    filler1 = CNABFieldAlfa("",length=9, default=" ", required=True)
    tipo_inscricao = CNABFieldInteger("",length=1, default="0", required=True)
    numero_inscricao = CNABFieldInteger("",length=14, default="0", required=True)
    convenio = CNABFieldInteger("",length=9, default="0", required=True)
    cobranca_cedente = CNABFieldInteger("",length=4, default="0014", required=True)
    carteira_cobranca = CNABFieldInteger("",length=2, default="11", required=True)
    variacao_carteira_cobranca = CNABFieldInteger("",length=3, default="222", required=True)
    reservado_bb = CNABFieldAlfa("",length=2, default=" ", required=True)
    agencia = CNABFieldInteger("",length=5, default="0", required=True)
    agencia_dv = CNABFieldAlfa("",length=1, default="", required=True)
    conta = CNABFieldInteger("",length=12, default="0", required=True)
    conta_dv = CNABFieldAlfa("",length=1, default="0", required=True)
    filler2 = CNABFieldAlfa("",length=1, default=" ", required=True)
    nome_empresa = CNABFieldAlfa("",length=30, default="", required=True)
    nome_banco = CNABFieldAlfa("",length=30,default="BANCO DO BRASIL S.A",required=True,)
    filler3 = CNABFieldAlfa("",length=10, default=" ", required=True)
    codigo_remessa = CNABFieldInteger("",length=1, default="1", required=True)
    data_geracao = CNABCreatedDateField("",length=8,required=True,)
    hora_geracao = CNABCreatedTimeField("",length=6,required=True,)
    numero_sequencial_arquivo = CNABFieldInteger("",length=6, default="0", required=True)
    versao_layout = CNABFieldInteger("",length=3, default="000", required=True)
    densidade_gravacao = CNABFieldInteger("",length=5, default="0", required=True)
    filler4 = CNABFieldAlfa("",length=20, default=" ", required=True)
    situacao_arquivo2 = CNABFieldAlfa("",length=20, default=" ", required=True)
    filler5 = CNABFieldAlfa("",length=14, default=" ", required=True)
    filler6 = CNABFieldAlfa("",length=3,  default="000",required=True,)
    filler7 = CNABFieldAlfa("",length=12, default=" ", required=True)


    def __init__(
        self,
        *,
        codigo_banco: Optional[Union[str, int]] = None,
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
        nome_banco: Optional[str] = None,
        codigo_remessa: Optional[Union[str, int]] = None,
        numero_sequencial_arquivo: Optional[Union[str, int]] = None,
        **kwargs):
        set_if_has_value(kwargs, 'codigo_banco', codigo_banco)
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
        set_if_has_value(kwargs, 'nome_banco', nome_banco)
        set_if_has_value(kwargs, 'codigo_remessa', codigo_remessa)
        set_if_has_value(kwargs, 'numero_sequencial_arquivo', numero_sequencial_arquivo)
        super().__init__(**kwargs)

    def inserir_lote(
        self,
        *,
        tipo_servico: Optional[Union[str, int]] = None,
        variacao: Optional[Union[str, int]] = None,
        **kwargs: dict) -> BancoBrasil240Registro1:
        set_if_has_value(kwargs, 'tipo_servico', tipo_servico)
        set_if_has_value(kwargs, 'variacao', variacao)
        return super().inserir_lote(**kwargs)
