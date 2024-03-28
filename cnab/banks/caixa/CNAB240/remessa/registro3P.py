from typing import Optional

from cnab.base.remessa import RegistroRemessa
from cnab.base.remessa.CNAB240 import CNAB240Registro3
from cnab.core.especie import CNABFieldEspecieTitulo
from cnab.core.field import (
    CNABFieldAlfa,
    CNABFieldDate,
    CNABFieldDecimal,
    CNABFieldInteger,
)

from .registro0 import Caixa240Registro0
from .registro1 import Caixa240Registro1
from .registro3Q import Caixa240Registro3Q
from .registro3R import Caixa240Registro3R
from .registro3S1e2 import Caixa240Registro3S1e2
from .registro3S3 import Caixa240Registro3S3


class Caixa240Registro3P(CNAB240Registro3):
    codigo_banco = CNABFieldInteger("", length=3, default="104", required=True)
    codigo_lote = CNABFieldInteger("", length=4, default=1, required=True)
    tipo_registro = CNABFieldInteger("", length=1, default="3", required=True)
    numero_registro = CNABFieldInteger("", length=5, default="0", required=True)
    seguimento = CNABFieldAlfa("", length=1, default="P", required=True)
    filler1 = CNABFieldAlfa("", length=1, default=" ", required=True)
    codigo_movimento = CNABFieldInteger("", length=2, default="01", required=True)
    agencia = CNABFieldInteger("", length=5, default="0", required=True)
    agencia_dv = CNABFieldAlfa("", length=1, default="", required=True)
    codigo_beneficiario = CNABFieldInteger("", length=7, default="", required=True)
    filler2 = CNABFieldInteger("", length=9, default="0", required=True)
    sinco = CNABFieldInteger("", length=1, default="0", required=True)
    nosso_numero = CNABFieldInteger("", length=17, default="0", required=True)
    codigo_carteira = CNABFieldInteger("", length=1, default="0", required=True)
    com_registro = CNABFieldInteger("", length=1, default="1", required=True)
    tipo_documento = CNABFieldInteger("", length=1, default="2", required=True)
    emissao_boleto = CNABFieldInteger("", length=1, default="1", required=True)
    entrega_boleto = CNABFieldInteger(
        "",
        length=1,
        default="1",
        required=True,
    )
    seu_numero = CNABFieldAlfa("", length=11, default=" ", required=True)
    filler3 = CNABFieldAlfa("", length=4, default=" ", required=True)
    data_vencimento = CNABFieldDate("", length=8, default="", required=True)
    valor = CNABFieldDecimal("", length=13, default="0", precision=2, required=True)
    agencia_cobradora = CNABFieldInteger("", length=5, default="0", required=True)
    agencia_cobradora_dv = CNABFieldInteger("", length=1, default="0", required=True)
    especie_titulo = CNABFieldEspecieTitulo("", length=2, required=True)
    aceite = CNABFieldAlfa("", length=1, default="N", required=True)
    data_emissao = CNABFieldDate("", length=8, default="", required=True)
    codigo_juros = CNABFieldInteger("", length=1, default="3", required=True)
    data_juros = CNABFieldDate("", length=8, default="0", required=True)
    vlr_juros = CNABFieldDecimal("", length=13, default="0", precision=2, required=True)
    codigo_desconto = CNABFieldInteger("", length=1, default="0", required=True)
    data_desconto = CNABFieldDate("", length=8, default="0", required=True)
    vlr_desconto = CNABFieldDecimal(
        "", length=13, default="0", precision=2, required=True
    )
    vlr_IOF = CNABFieldDecimal("", length=13, default="0", precision=2, required=True)
    vlr_abatimento = CNABFieldDecimal(
        "", length=13, default="0", precision=2, required=True
    )
    seu_numero2 = CNABFieldAlfa("", length=25, default=" ", required=True)
    protestar = CNABFieldAlfa("", length=1, default="3", required=True)
    prazo_protesto = CNABFieldInteger("", length=2, default="0", required=True)
    baixar = CNABFieldInteger("", length=1, default="0", required=True)
    prazo_baixar = CNABFieldInteger("", length=3, default="0", required=True)
    codigo_moeda = CNABFieldInteger("", length=2, default="9", required=True)
    filler4 = CNABFieldInteger("", length=10, default="0", required=True)
    filler5 = CNABFieldAlfa("", length=1, default=" ", required=True)

    def _inserir_desconto_mensagem(self, **kwargs):
        desconto2 = kwargs.get("codigo_desconto2")
        desconto3 = kwargs.get("codigo_desconto3")
        mensagem = kwargs.get("mensagem")
        if not desconto2 and not desconto3 and not mensagem:
            return

        Caixa240Registro3R(self.header, self, self.lote, **kwargs)

    def _inserir_detalhe(self, **kwargs: dict):
        Caixa240Registro3Q(self.header, self, self.lote, **kwargs)
        self._inserir_desconto_mensagem(**kwargs)

        if int(kwargs.get("emissao_boleto")) != 1:
            return

        if kwargs.get("mensagem_frente"):
            kwargs["mensagem_140"] = kwargs.get("mensagem_frente")
            kwargs["tipo_impressao"] = 1
            Caixa240Registro3S1e2(self.header, self, self.lote, **kwargs)

        if kwargs.get("mensagem_verso"):
            kwargs["mensagem_140"] = kwargs.get("mensagem_verso")
            kwargs["tipo_impressao"] = 2
            Caixa240Registro3S1e2(self.header, self, self.lote, **kwargs)

        if (
            not kwargs.get("mensagem_5")
            and not kwargs.get("mensagem_6")
            and not kwargs.get("mensagem_7")
            and not kwargs.get("mensagem_8")
        ):
            return
        Caixa240Registro3S3(self.header, self, self.lote, **kwargs)

    def __init__(
        self,
        header: Optional[Caixa240Registro0],
        parent: Optional[RegistroRemessa],
        lote: Caixa240Registro1,
        **kwargs: dict,
    ):
        super().__init__(header, parent, lote, **kwargs)

        self._inserir_detalhe(**kwargs)
