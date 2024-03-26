from typing import Optional
from cnab.base.cnab_240 import CNAB240Registro3
from cnab.core.field import CNABFieldInteger, CNABFieldAlfa, CNABFieldDate, CNABFieldDecimal
from cnab.core.especie import CNABFieldEspecieTitulo
from cnab.base.registro import Registro
from cnab.utils.check_digit import compute_check_digit
from .registro3Q import Santander240Registro3Q
from .registro1 import Santander240Registro1
from .registro3R import Santander240Registro3R

class Santander240Registro3P(CNAB240Registro3):
    codigo_banco = CNABFieldInteger("",length=3, default="033", required=True)
    codigo_lote = CNABFieldInteger("",length=4, default=1, required=True)
    tipo_registro = CNABFieldInteger("",length=1, default="3", required=True)
    numero_registro = CNABFieldInteger("",length=5, default="0", required=True)
    seguimento = CNABFieldAlfa("",length=1, default="P", required=True)
    filler1 = CNABFieldAlfa("",length=1, default=" ", required=True)
    codigo_movimento = CNABFieldInteger("",length=2,default="01",required=True,)
    agencia = CNABFieldInteger("",length=4, default="", required=True)
    agencia_dv = CNABFieldInteger("",length=1, default="", required=True)
    conta = CNABFieldInteger("",length=9, default="0", required=True)
    conta_dv = CNABFieldInteger("",length=1, default="", required=True)
    codigo_beneficiario = CNABFieldInteger("",length=9, default="", required=True, value_from='conta')
    codigo_beneficiario_dv = CNABFieldInteger("",length=1, default="", required=True, value_from='conta_dv')
    filler2 = CNABFieldAlfa("",length=2, default=" ", required=True)
    nosso_numero = CNABFieldInteger("",length=13, default="", required=True)
    tipo_cobranca = CNABFieldInteger("",length=1, default="5", required=True)
    forma_cadastramento = CNABFieldInteger("",length=1,default="1",required=True,)
    tipo_documento = CNABFieldInteger("",length=1,default="1",required=True,)
    filler3 = CNABFieldAlfa("",length=1, default=" ", required=True)
    filler4 = CNABFieldAlfa("",length=1, default=" ", required=True)
    seu_numero = CNABFieldInteger("",length=15, default="", required=True)
    data_vencimento = CNABFieldDate("",length=8, default="", required=True)
    valor = CNABFieldDecimal("",length=13,default="",precision=2,required=True,)
    agencia_cobradora = CNABFieldInteger("",length=4, default="0", required=True)
    agencia_cobradora_dv = CNABFieldInteger("",length=1, default="0", required=True)
    filler5 = CNABFieldAlfa("",length=1, default=" ", required=True)
    especie_titulo = CNABFieldEspecieTitulo("",length=2, required=True)
    aceite = CNABFieldAlfa("",length=1, default="N", required=True)
    data_emissao = CNABFieldDate("",length=8, default="", required=True)
    codigo_juros = CNABFieldInteger("",length=1, default="0", required=True)
    data_juros = CNABFieldDate("",length=8, default="0", required=True)
    vlr_juros = CNABFieldDecimal("",length=13,default="0",precision=2,required=True,)
    codigo_desconto = CNABFieldInteger("",length=1, default="0", required=True)
    data_desconto = CNABFieldDate("",length=8, default="0", required=True)
    vlr_desconto = CNABFieldDecimal("",length=13,default="0",precision=2,required=True,)
    vlr_IOF = CNABFieldDecimal("",length=13,default="0",precision=2,required=True,)
    vlr_abatimento = CNABFieldDecimal("",length=13,default="0",precision=2,required=True,)
    seu_numero2 = CNABFieldAlfa("",length=25, default=" ", required=True)
    protestar = CNABFieldAlfa("",length=1, default=3, required=True)
    prazo_protesto = CNABFieldInteger("",length=2, default="0", required=True)
    baixar = CNABFieldInteger("",length=1, default="1", required=True)
    filler6 = CNABFieldInteger("",length=1, default="0", required=True)
    prazo_baixar = CNABFieldInteger("",length=2, default="90", required=True)
    codigo_moeda = CNABFieldInteger("",length=2, default="00", required=True)
    filler7 = CNABFieldAlfa("",length=11, default=" ", required=True)


    def _inserir_detalhe(self, **kwargs: dict):
        if int(kwargs.get('codigo_movimento')) == 2:
            return
        
        Santander240Registro3Q(self.header, self, self.lote, **kwargs)
        
        desconto2 = kwargs.get('codigo_desconto2')
        desconto3 = kwargs.get('codigo_desconto3')
        vlr_multa = kwargs.get('vlr_multa')
        informacao_pagador = kwargs.get('informacao_pagador')
        if not desconto2 and not desconto3 and not vlr_multa and not informacao_pagador:
            return
        
        Santander240Registro3R(self.header, self, self.lote, **kwargs)

    def __init__(
        self,
        header: Optional["Registro"],
        parent: Optional["Registro"],
        lote: Santander240Registro1,
        **kwargs: dict
    ):
        super().__init__(header, parent, lote, **kwargs)

        self._inserir_detalhe(**kwargs)

    def get_nosso_numero(self):
        if not self.nosso_numero:
            return "0"
        num = str(self.nosso_numero)
        if num == "0" or num == " ":
            return num
        return num + str(compute_check_digit(num))
