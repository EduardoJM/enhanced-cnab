from typing import Optional, Union
from cnab.base.remessa import Remessa
from .registro0 import BancoBrasil240Registro0
from .registro9 import BancoBrasil240Registro9

class CNAB240BancoBrasil(Remessa):
    header: BancoBrasil240Registro0
    registro0_class = BancoBrasil240Registro0
    registro9_class = BancoBrasil240Registro9

    def __init__(
        self,
        *,
        codigo_banco: Optional[Union[str, int]] = "001",
        codigo_lote: Optional[Union[str, int]] = "0000",
        tipo_registro: Optional[Union[str, int]] = "0",
        tipo_inscricao: Optional[Union[str, int]] = "0",
        numero_inscricao: Optional[Union[str, int]] = "0",
        convenio: Optional[Union[str, int]] = "0",
        cobranca_cedente: Optional[Union[str, int]] = "0014",
        carteira_cobranca: Optional[Union[str, int]] = "11",
        variacao_carteira_cobranca: Optional[Union[str, int]] = "222",
        agencia: Optional[Union[str, int]] = "0",
        agencia_dv: Optional[Union[str, int]] = "",
        conta: Optional[Union[str, int]] = "0",
        conta_dv: Optional[Union[str, int]] = "0",
        nome_empresa: Optional[str] = "",
        nome_banco: Optional[str] = "BANCO DO BRASIL S.A",
        codigo_remessa: Optional[Union[str, int]] = "1",
        numero_sequencial_arquivo: Optional[Union[str, int]] = "0",
        **kwargs,
    ):
        kwargs.set('codigo_banco', codigo_banco)
        kwargs.set('codigo_lote', codigo_lote)
        kwargs.set('tipo_registro', tipo_registro)
        kwargs.set('tipo_inscricao', tipo_inscricao)
        kwargs.set('numero_inscricao', numero_inscricao)
        kwargs.set('convenio', convenio)
        kwargs.set('cobranca_cedente', cobranca_cedente)
        kwargs.set('carteira_cobranca', carteira_cobranca)
        kwargs.set('variacao_carteira_cobranca', variacao_carteira_cobranca)
        kwargs.set('agencia', agencia)
        kwargs.set('agencia_dv', agencia_dv)
        kwargs.set('conta', conta)
        kwargs.set('conta_dv', conta_dv)
        kwargs.set('nome_empresa', nome_empresa)
        kwargs.set('nome_banco', nome_banco)
        kwargs.set('codigo_remessa', codigo_remessa)
        kwargs.set('numero_sequencial_arquivo', numero_sequencial_arquivo)
        super().__init__(**kwargs)

    def inserir_lote(self, **kwargs):
        # TODO: implement kwargs named here
        return super().inserir_lote(**kwargs)
