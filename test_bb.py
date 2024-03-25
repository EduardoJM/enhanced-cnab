from datetime import date
from cnab.banks.banco_brasil import CNAB240BancoBrasil
from cnab.core.especie import EspecieTitulo

cnab = CNAB240BancoBrasil(
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
)
lote = cnab.inserir_lote(tipo_servico=1, variacao="027")
cobranca = lote.inserir_detalhe(
    # Registro 3P Dados do Boleto
    nosso_numero="1800001",  # numero sequencial de boleto
    # Consulte a pág. 9 da documentação para mais informações sobre o nosso número
    #'nosso_numero_dv'   =	1, # pode ser informado ou calculado pelo sistema
    parcela="01",
    modalidade="1",
    tipo_formulario="4",
    codigo_carteira="4",  # codigo da carteira ()
    # 1 – para carteira 11/12 na modalidade Simples
    # 2 ou 3 – para carteira 11/17 modalidade Vinculada/Caucionada e carteira 31
    # 4 – para carteira 11/17 modalidade Descontada e carteira 51
    # 7 – para carteira 17 modalidade Simples
    emissao_boleto=2,  # tipo de emissao do boleto informar 2 para emissao pelo beneficiario e 1 para emissao pelo banco
    carteira="17",  # codigo da carteira
    seu_numero="DEV180001",  # se nao informado usarei o nosso numero
    data_vencimento=date(2018, 4, 30),  # informar a data neste formato AAAA-MM-DD
    valor="5.00",  # Valor do boleto como float valido em php
    cod_emissao_boleto="2",  # tipo de emissao do boleto informar 2 para emissao pelo beneficiario e 1 para emissao pelo banco
    especie_titulo=EspecieTitulo.DuplicataMercantil,
    data_emissao=date(2018, 4, 5),  # informar a data neste formato AAAA-MM-DD
    codigo_juros="2",  # Taxa por mês,
    data_juros=date(2018, 4, 30),  # data dos juros, mesma do vencimento
    vlr_juros="0000000000001.00",  # Valor do juros/mora informa 1% e o sistema recalcula a 0,03% por
    # Você pode inserir desconto se houver, ou deixar em branco
    #'codigo_desconto'	=	'1',
    #'data_desconto'		= 	'2018-04-15', # inserir data para calcular desconto
    #'vlr_desconto'		= 	'0', # Valor do desconto
    #'vlr_IOF'			= 	'0',
    protestar="1",  # 1 = Protestar com (Prazo) dias, 3 = Devolver após (Prazo) dias
    prazo_protesto="90",  # Informar o numero de dias apos o vencimento para iniciar o protesto
    identificacao_contrato="0000000000",  # Campo não tratado pelo sistema. Pode ser informado 'zeros' ou o número do contrato de cobrança.
    # Registro 3Q [PAGADOR]
    tipo_inscricao="1",  # campo fixo, escreva '1' se for pessoa fisica, 2 se for pessoa juridica
    numero_inscricao="63803588464",  # cpf ou ncpj do pagador
    nome_pagador="Elias Alves",  # O Pagador é o cliente, preste atenção nos campos abaixo
    endereco_pagador="Rua Esquerda, 42",
    bairro_pagador="Bairro Queluz",
    cep_pagador="36400000",  # com hífem
    cidade_pagador="Conselheiro Lafaiete",
    uf_pagador="MG",
    # Registro 3R Multas, descontos, etc
    # Você pode inserir desconto se houver, ou deixar em branco, mas quando informar
    # deve preencher os 3 campos: codigo, data e valor
    codigo_multa="2",  # Taxa por mês
    data_multa=date(2018, 4, 30),  # data dos juros, mesma do vencimento
    vlr_multa="0000000000002.00",  # Valor do juros de 2% ao mês
    # Registro 3S3 Mensagens a serem impressas
    mensagem_fixa1="Após venc. Mora 0,03%/dia e Multa 2,00%",
    mensagem_fixa2="Não conceder desconto",
    mensagem_3="Sujeito a protesto após o vencimento",
    mensagem_4="VelvetTux Soluções em Sistemas <('')",
    codigo_banco_correspondente="001",
)

lines = cnab.get_text()
with open("bb.rem", "w") as f:
    f.write("\r\n".join(lines))
