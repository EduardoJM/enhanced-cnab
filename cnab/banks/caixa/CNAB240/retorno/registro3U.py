from cnab.base.retorno.CNAB240 import Registro3Retorno
from cnab.core.field import CNABFieldInteger, CNABFieldAlfa, CNABFieldDate, CNABFieldDecimal

class CaixaRetornoCnab240Registro3U(Registro3Retorno):
    codigo_banco = CNABFieldInteger("", 
        length=3,
        default='104',
        required=True)
    codigo_lote = CNABFieldInteger("", 
        length=4,
        default=1,
        required=True)
    tipo_registro = CNABFieldInteger("", 
        length=1,
        default='3',
        required=True)
    numero_registro = CNABFieldInteger("", 
        length=5,
        default='0',
        required=True)
    seguimento = CNABFieldAlfa("", 
        length=1,
        default='U',
        required=True)
    filler1 = CNABFieldInteger("", 
        length=1,
        default=' ',
        required=True)
    codigo_movimento = CNABFieldInteger("", 
        length=2,
        default='',
        required=True)
    vlr_juros_multa = CNABFieldDecimal("", 
        length=13,
        default='',
        precision=2,
        required=True)
    vlr_desconto = CNABFieldDecimal("", 
        length=13,
        default='',
        precision=2,
        required=True)
    vlr_abatimento = CNABFieldDecimal("", 
        length=13,
        default='',
        precision=2,
        required=True)
    vlr_IOF = CNABFieldDecimal("", 
        length=13,
        default='',
        precision=2,
        required=True)
    vlr_pago = CNABFieldDecimal("", 
        length=13,
        default='',
        precision=2,
        required=True)
    vlr_liquido = CNABFieldDecimal("", 
        length=13,
        default='',
        precision=2,
        required=True)
    vlr_outras_despesas = CNABFieldDecimal("", length=13,default=' ',precision=2,required=True)
    vlr_outros_creditos = CNABFieldDecimal("", length=13,default='',precision=2,required=True)
    data_ocorrencia = CNABFieldDate("", length=8,default='',required=True)
    data_credito = CNABFieldDate("", length=8,default='0',required=True)
    filler2 = CNABFieldInteger("", length=4,default='',required=True)
    data_debito_tarifa = CNABFieldDate("",length=8,default=' ',required=True)
    codigo_banco_pagador = CNABFieldAlfa("", length=15,default=' ',required=True)
    filler4 = CNABFieldAlfa("", length=30,default=' ',required=True)
