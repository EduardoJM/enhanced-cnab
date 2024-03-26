from cnab.utils.auto_identify_retorno import auto_identify_retorno_file

with open('./retorno_cnab240_caixa.ret', 'r') as f:
    text = f.read()

file = auto_identify_retorno_file(text)
print(file)

with open('./retorno_cnab400_itau.ret', 'r') as f:
    text = f.read()

file = auto_identify_retorno_file(text)
print(file)
