from datetime import date
from cnab.banks.BB.CNAB240.header import BancoBrasil240Header
from cnab.banks.BB.CNAB240.lote import BancoBrasil240Lote
# from cnab.banks.BB.CNAB240.cobranca import Santander240Cobranca
# from cnab.banks.BB.CNAB240.footer import Santander240Footer

header = BancoBrasil240Header(
    None,
    None,
    tipo_inscricao="1",  # 1 para cpf, 2 cnpj
    numero_inscricao="70116028106",  # seu cpf ou cnpj completo
    agencia="324",  # agencia sem o digito verificador
    agencia_dv="7",  # somente o digito verificador da agencia
    conta="59237",  # número da conta
    conta_dv="4",  # digito da conta
    nome_empresa="Empresa ABC",  # seu nome de empresa
    numero_sequencial_arquivo="00000",  # Deve ter no máximo 5 dígitos, pode ficar com zeros.
    convenio="106608",  # codigo fornecido pelo banco
    carteira="17",  # codigo fornecido pelo banco
    situacao_arquivo="",  # Deve ficar em branco para ser aceito. (TS para testes)
    uso_bb1="009999999001411222",  # Deve ter 18 dígitos
)
lote = BancoBrasil240Lote(
    header,
    header,
    tipo_servico=1,
    variacao='027'
)

lines = header.get_text()
with open('bb.rem', 'w') as f:
    f.write('\r\n'.join(lines))
