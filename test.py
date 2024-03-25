# from .cnab.remessa import Remessa
from datetime import date
from cnab.banks.santander import CNAB240Santander
from cnab.core.especie import EspecieTitulo

cnab = CNAB240Santander(
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
lote = cnab.inserir_lote(
    tipo_servico=1,
    codigo_transmissao='12345678901234567890'
)
cobranca = lote.inserir_detalhe(
    conta_cobranca= '12345678', # número da conta cobranca obs(verificar se eh o mesmo da conta movimento)
    data_segundo_desconto= '',
    codigo_movimento=  1, # 1 = Entrada de título, para outras opções ver nota explicativa C004 manual Cnab_SIGCB na pasta docs
    nosso_numero=  50, # numero sequencial de boleto
    seu_numero= 43,# se nao informado usarei o nosso numero
    # campos necessarios somente para itau e siccob,  não precisa comentar se for outro layout
    carteira_banco= 109, # codigo da carteira ex: 109,RG esse vai o nome da carteira no banco
    codigo_carteira="01", # I para a maioria ddas carteiras do itau
    # campos necessarios somente para itau,  não precisa comentar se for outro layout
    especie_titulo = EspecieTitulo.DuplicataMercantil,
    valor          = 100.00, # Valor do boleto como float valido em php
    emissao_boleto = 2, # tipo de emissao do boleto informar 2 para emissao pelo beneficiario e 1 para emissao pelo banco
    protestar      = 3, # 1 = Protestar com (Prazo) dias, 3 = Devolver após (Prazo) dias
    prazo_protesto = 5, # Informar o numero de dias apos o vencimento para iniciar o protesto
    nome_pagador   = "JOSÉ da SILVA ALVES", # O Pagador é o cliente, preste atenção nos campos abaixo
    tipo_inscricao = 1, # campo fixo, escreva '1' se for pessoa fisica, 2 se for pessoa juridica
    numero_inscricao= '12312212356',#cpf ou ncpj do pagador
    endereco_pagador= 'Rua dos developers,123 sl 103',
    bairro_pagador = 'Bairro da insonia',
    cep_pagador    = '12345123', # com hífem
    cidade_pagador = 'Londrina',
    uf_pagador     = 'PR',
    data_vencimento= date(2016, 4, 9), # informar a data neste formato
    data_emissao   = date(2016, 4, 9), # informar a data neste formato
    vlr_juros      = 0.15, # Valor do juros de 1 dia'
    data_desconto  = date(2016, 4, 9), # informar a data neste formato
    vlr_desconto   = '0', # Valor do desconto
    baixar         = 1, # codigo para indicar o tipo de baixa '1' (Baixar/ Devolver) ou '2' (Não Baixar / Não Devolver)
    prazo_baixa    = 90, # prazo de dias para o cliente pagar após o vencimento
    mensagem       = 'JUROS de R$0,15 ao dia. Não receber apos 30 dias',
    email_pagador  = 'rogerio@ciatec.net',
    data_multa     = date(2016, 4, 9), # informar a data neste formato, # data da multa
    vlr_multa      = 30.00, # valor da multa
    codigo_juros   = 3,
    # campos necessários somente para o sicoob
    taxa_multa=30.00, # taxa de multa em percentual
    taxa_juros=30.00, # taxa de juros em percentual
)

cobranca = lote.inserir_detalhe(
    conta_cobranca ='12345678', # número da conta cobranca obs(verificar se eh o mesmo da conta movimento)
    data_segundo_desconto ='', 
    codigo_movimento =1, #1 = Entrada de título, para outras opções ver nota explicativa C004 manual Cnab_SIGCB na pasta docs
    nosso_numero      =50, # numero sequencial de boleto
    seu_numero        =43,# se nao informado usarei o nosso numero

    # campos necessarios somente para itau e siccob,  não precisa comentar se for outro layout    */
    carteira_banco    =109, # codigo da carteira ex: 109,RG esse vai o nome da carteira no banco
    cod_carteira      ="01", # I para a maioria ddas carteiras do itau
     # campos necessarios somente para itau,  não precisa comentar se for outro layout    */

    especie_titulo    =1, #"DM", # informar dm e sera convertido para codigo em qualquer laytou conferir em especie.php
    valor             =100.00, # Valor do boleto como float valido em php
    emissao_boleto    =2, # tipo de emissao do boleto informar 2 para emissao pelo beneficiario e 1 para emissao pelo banco
    protestar         =3, # 1 = Protestar com (Prazo) dias, 3 = Devolver após (Prazo) dias
    prazo_protesto    =5, # Informar o numero de dias apos o vencimento para iniciar o protesto
    nome_pagador      ="JOSÉ da SILVA ALVES", # O Pagador é o cliente, preste atenção nos campos abaixo
    tipo_inscricao    =1, #campo fixo, escreva '1' se for pessoa fisica, 2 se for pessoa juridica
    numero_inscricao  ='12312212356',#cpf ou ncpj do pagador
    endereco_pagador  ='Rua dos developers,123 sl 103',
    bairro_pagador    ='Bairro da insonia',
    cep_pagador       ='12345123', # com hífem
    cidade_pagador    ='Londrina',
    uf_pagador        ='PR',
    data_vencimento   =date(2016, 4, 9), # informar a data neste formato
    data_emissao      =date(2016, 4, 9), # informar a data neste formato
    vlr_juros         =0.15, # Valor do juros de 1 dia'
    data_desconto     =date(2016, 4, 9), # informar a data neste formato
    vlr_desconto      ='0', # Valor do desconto
    baixar            =1, # codigo para indicar o tipo de baixa '1' (Baixar/ Devolver) ou '2' (Não Baixar / Não Devolver)
    prazo_baixar       =90, # prazo de dias para o cliente pagar após o vencimento
    mensagem          ='JUROS de R$0,15 ao dia. Não receber apos 30 dias',
    email_pagador     ='rogerio@ciatec.net', # data da multa
    data_multa        =date(2016, 4, 9), # informar a data neste formato, # data da multa
    vlr_multa         =30.00, # valor da multa
)

lines = cnab.get_text()
with open('remessa-test.rem', 'w') as f:
    f.write('\r\n'.join(lines))
