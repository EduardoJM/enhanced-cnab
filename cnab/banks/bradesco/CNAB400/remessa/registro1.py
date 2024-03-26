from typing import Optional
from cnab.base.remessa.CNAB400 import CNAB400Registro1
from cnab.core.field import CNABFieldInteger, CNABFieldAlfa, CNABFieldDecimal, CNABFieldDate
from cnab.core.especie import CNABFieldEspecieTitulo
from cnab.base.remessa import RegistroRemessa

class BradescoCnab400Registro1(CNAB400Registro1):
    tipo_registro = CNABFieldInteger("001-001", length=1, default='1', required=True)
    agencia_debito = CNABFieldInteger("002-006", length=5, default='0', required=True)
    digito_agencia_debito = CNABFieldInteger("007-007", length=1, default='0', required=True)
    razao_conta_corrente_pagador = CNABFieldInteger("008-012", length=5, default='0', required=True)
    conta_corrente_pagador = CNABFieldInteger("013-019", length=7, default='0', required=True)
    digito_conta_corrente_pagador = CNABFieldInteger("020-020", length=1, default='0', required=True)
    filler0 = CNABFieldInteger("021-021", length=1, default='0', required=True)
    carteira_banco = CNABFieldInteger("022-024", length=3, default='0', required=True)
    agencia = CNABFieldInteger("025-029", length=5, default='0', required=True)
    conta = CNABFieldInteger("030-036", length=7, default='0', required=True)
    conta_dv = CNABFieldInteger("037-037", length=1, default='0', required=True)
    seu_numero = CNABFieldAlfa("038-062", length=25, default=' ', required=True)
    codigo_banco_debito = CNABFieldInteger("063-065", length=3, default='0', required=True)
    codigo_multa = CNABFieldInteger("066-066", length=1, default='0', required=True)
    taxa_multa = CNABFieldDecimal("067-070", length=2, default='0', precision=2, required=True)
    nosso_numero = CNABFieldInteger("071-081", length=11, default='0', required=True)
    nosso_numero_dv = CNABFieldAlfa("082-082", length=1, default='0', required=True)
    vlr_bonificacao_dia = CNABFieldDecimal("083-092", length=8, default='0', precision=2, required=True)
    emissao_boleto = CNABFieldInteger("093-093", length=1, default='2', required=True)
    debito_automatico = CNABFieldAlfa("094-094", length=1, default='N', required=True)
    filler6 = CNABFieldAlfa("095-104", length=10, default=' ', required=True)
    indicador_rateio = CNABFieldAlfa("105-105", length=1, default=' ', required=True)
    endereco_aviso_debito = CNABFieldInteger("106-106", length=1, default='2', required=True)
    filler7 = CNABFieldAlfa("107-108", length=2, default=' ', required=True)
    codigo_movimento = CNABFieldInteger("109-110", length=2, default=1, required=True)
    numero_documento = CNABFieldAlfa("111-120", length=10, default=' ', required=True)
    data_vencimento = CNABFieldDate("121-126", length=6, default='', required=True)
    valor = CNABFieldDecimal("127-139", length=11, default='', precision=2, required=True)
    banco_cobrador = CNABFieldInteger("140-142", length=3, default='0', required=True)
    agencia_cobradora = CNABFieldInteger("143-147", length=5, default='0', required=True)
    especie_titulo = CNABFieldEspecieTitulo("148-149", length=2, required=True)
    aceite = CNABFieldAlfa("150-150", length=1, default='N', required=True)
    data_emissao = CNABFieldDate("151-156", length=6, default='', required=True)
    cod_instrucao1 = CNABFieldInteger("157-158", length=2, default='0', required=True)
    cod_instrucao2 = CNABFieldInteger("159-160", length=2, default='0', required=True)
    vlr_juros = CNABFieldDecimal("161-173", length=11, default='0', precision=2, required=True)
    data_desconto = CNABFieldDate("174-179", length=6, default='0', required=True)
    vlr_desconto = CNABFieldDecimal("180-192", length=11, default='0', precision=2, required=True)
    vlr_IOF = CNABFieldDecimal("193-205", length=11, default='0', precision=2, required=True)
    vlr_abatimento = CNABFieldDecimal("206-218", length=11, default='0', precision=2, required=True)
    tipo_inscricao = CNABFieldInteger("219-220", length=2, default='', required=True)
    numero_inscricao = CNABFieldInteger("221-234", length=14, default='', required=True)
    nome_pagador = CNABFieldAlfa("235-274", length=40, default='', required=True)
    endereco_pagador = CNABFieldAlfa("275-314", length=40, default='', required=True)
    mensagem1 = CNABFieldAlfa("315-326", length=12, default=' ', required=True)
    cep_pagador = CNABFieldInteger("327-334", length=8, default='', required=True)
    mensagem2 = CNABFieldAlfa("334-394", length=60, default=' ', required=True)
    numero_registro = CNABFieldInteger("395-400", length=6, default='0', required=True)

    def __init__(self, header: Optional[RegistroRemessa], parent: Optional[RegistroRemessa], **kwargs: dict):
        super().__init__(header, parent, **kwargs)

    def inserir_mensagem(self, **kwargs):
        if not kwargs.get('mensagem'):
            return
        from .registro2 import BradescoCnab400Registro2
        return BradescoCnab400Registro2(self.header, self, kwargs)
