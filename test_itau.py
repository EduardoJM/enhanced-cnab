from datetime import date

from cnab.banks.itau import CNAB400Itau
from cnab.core.especie import EspecieTitulo

cnab = CNAB400Itau(
    agencia="324",  # agencia sem o digito verificador
    conta="59237",  # número da conta
    conta_dv="4",  # digito da conta
    nome_empresa="Empresa ABC",  # seu nome de empresa
)

lote = cnab.inserir_lote()

lote.inserir_detalhe(
    tipo_inscricao_empresa="2",
    numero_inscricao_empresa="39845082000100",
    nosso_numero="1800001",
    data_emissao=date(2018, 4, 5),
    data_vencimento=date(2018, 4, 5),
    data_multa=date(2018, 4, 5),
    valor=450.40,
    tipo_inscricao="1",
    numero_inscricao="70116028106",
    nome_pagador="EDUARDO OLIVEIRA",
    endereco_pagador="RUA JANDIRA LEAO CUNHA",
    bairro_pagador="JK Nova Capital",
    cep_pagador="75140430",
    cidade_pagador="Anápolis",
    uf_pagador="GO",
    cod_instrucao1="10",
    data_desconto=date(2018, 4, 5),
    prazo_baixa=30,
    especie_titulo=EspecieTitulo.DuplicataMercantil,
)
lote.inserir_detalhe(
    cod_instrucao1="09",
    cod_instrucao2="32",
    prazo_baixa=30,
    vlr_juros=1.95,
    tipo_inscricao_empresa="2",
    numero_inscricao_empresa="39845082000100",
    especie_titulo=EspecieTitulo.DuplicataMercantil,
    nosso_numero="1800001",
    data_emissao=date(2018, 4, 5),
    data_vencimento=date(2018, 4, 5),
    data_desconto=date(2018, 4, 5),
    valor=450.40,
    tipo_inscricao="1",
    numero_inscricao="70116028106",
    nome_pagador="EDUARDO OLIVEIRA",
    endereco_pagador="RUA JANDIRA LEAO CUNHA",
    bairro_pagador="JK Nova Capital",
    cep_pagador="75140430",
    cidade_pagador="Anápolis",
    uf_pagador="GO",
)

lines = cnab.get_text()
with open("itau.rem", "w") as f:
    f.write("\r\n".join(lines))
