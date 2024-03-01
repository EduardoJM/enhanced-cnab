from datetime import date
from cnab.banks.itau import CNAB400Itau
from cnab.core.especie import EspecieTitulo

cnab = CNAB400Itau(
    agencia="324",  # agencia sem o digito verificador
    conta="59237",  # número da conta
    conta_dv="4",  # digito da conta
    nome_empresa="Empresa ABC",  # seu nome de empresa
    numero_sequencial="1",  # Deve ter no máximo 5 dígitos, pode ficar com zeros.
)


lines = cnab.get_text()
with open("itau.rem", "w") as f:
    f.write("\r\n".join(lines))
