# from .cnab.remessa import Remessa
from cnab.banks.santander.CNAB240.header import Santander240Header
from cnab.banks.santander.CNAB240.lote import Santander240Lote

ctb = Santander240Header(
    None,
    nome_empresa="Empresa ABC",
    tipo_inscricao=2,
    numero_inscricao="12312212356",
    agencia=3300,
    agencia_dv=6,
    conta=12345678,
    conta_dv=9,
    codigo_transmissao='12345678901234567890',
    codigo_beneficiario=10668,
    codigo_beneficiario_dv=2,
    numero_sequencial_arquivo=1
)
lote = Santander240Lote(
    ctb,
    tipo_servico=1,
    codigo_transmissao='12345678901234567890'
)

ctb.append(lote)

lines = ctb.get_text()
#print(txt)
#print(len(txt))

with open('remessa-test.rem', 'w') as f:
    f.write('\r\n'.join(lines))
