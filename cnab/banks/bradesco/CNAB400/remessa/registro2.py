from cnab.base.cnab_400 import CNAB400Registro2
from cnab.core.field import CNABFieldInteger, CNABFieldAlfa, CNABFieldDate, CNABFieldDecimal


class BradescoCnab400Registro2(CNAB400Registro2):
    tipo_registro = CNABFieldInteger("001-001", length=1, default="2", required=True)
    mensagem_1 = CNABFieldAlfa("002-081", length=80, default=" ", required=True)
    mensagem_2 = CNABFieldAlfa("082-161", length=80, default=" ", required=True)
    mensagem_3 = CNABFieldAlfa("162-241", length=80, default=" ", required=True)
    mensagem_4 = CNABFieldAlfa("242-321", length=80, default=" ", required=True)
    data_desconto = CNABFieldAlfa("322-327", length=6, default="0", required=True)
    vlr_desconto = CNABFieldDecimal("328-340", length=11, default="0", precision=2, required=True)
    data_desconto_2 = CNABFieldDate("341-346", length=6, default="0", required=True)
    vlr_desconto_2 = CNABFieldDecimal("347-359", length=11, default="0", precision=2, required=True)
    filler = CNABFieldAlfa("360-366", length=7, default=" ", required=True)
    carteira_banco = CNABFieldInteger("367-369", length=3, default="0", required=True)
    agencia = CNABFieldInteger("370-374", length=5, default="0", required=True)
    conta = CNABFieldInteger("375-381", length=7, default="0", required=True)
    conta_dv = CNABFieldInteger("382-382", length=1, default="0", required=True)
    nosso_numero = CNABFieldInteger("383-393", length=11, default="0", required=True)
    nosso_numero_dv = CNABFieldAlfa("394-394", length=1, default="0", required=True)
    numero_registro = CNABFieldInteger("395-400", length=6, default="0", required=True)
