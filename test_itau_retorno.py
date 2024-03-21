from cnab.banks.itau import CNAB400ItauRetorno

with open('./retorno_cnab400_itau.ret', 'r') as f:
    text = f.read()

ret = CNAB400ItauRetorno(text)
lotes = ret.children

for lote in lotes:
    print(lote)
    registros = lote.children
    for reg in registros:
        print(reg.codigo_movimento)
        print("- ", reg.valor)
        print(reg.vlr_pago)
