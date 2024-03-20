from cnab.banks.itau import CNAB400ItauRetorno

with open('./retorno_cnab400_itau.ret', 'r') as f:
    text = f.read()

ret = CNAB400ItauRetorno(text)
