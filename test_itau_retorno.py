from cnab.banks.itau import CNAB400ItauRetorno
from cnab.banks.itau.CNAB400.retorno.registro0 import ItauRetornoCnab400Registro0

with open('./retorno_cnab400_itau.ret', 'r') as f:
    text = f.read()

ret = CNAB400ItauRetorno(text)
lotes = ret.children

for lote in lotes:
    if not isinstance(lote, ItauRetornoCnab400Registro0):
        continue

    print(lote.codigo_banco)
    print(lote.literal_servico)
    registros = lote.children
    for reg in registros:
        reg.tipo_registro
        print(reg.codigo_movimento)
        print("- ", reg.valor)
        print(reg.vlr_pago)
