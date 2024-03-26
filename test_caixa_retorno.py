from cnab.banks.caixa import CNAB400CaixaRetorno
from cnab.banks.caixa.CNAB240.retorno.registro0 import CaixaRetornoCnab240Registro0

with open('./retorno_cnab240_caixa.ret', 'r') as f:
    text = f.read()

ret = CNAB400CaixaRetorno(text)
lotes = ret.children

for lote in lotes:
    if not isinstance(lote, CaixaRetornoCnab240Registro0):
        continue

    print(lote.versao_layout)

    print(lote.codigo_banco)
    registros = lote.children
    for reg in registros:
        for child in reg.children:
            print(child.codigo_movimento)
