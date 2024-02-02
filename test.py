# from .cnab.remessa import Remessa
from cnab.banks.santander.CNAB240.header import Santander240Header

"""
cls = Remessa(
    104,
    "cnab240_SIGCB",
    nome_empresa="Empresa ABC",
    tipo_inscricao=2,
    numero_inscricao="70116028106",
    agencia=1234,
    agencia_dv=1,
    conta=12345,
    conta_dv=1,
    codigo_beneficiario=123456,
    numero_sequencial_arquivo=1
)

class Registro0(RegistroRem):
    def get_value(self, key, default):
        from datetime import datetime
        if key == "data_geracao":
            print(len(datetime.now().strftime("%Y-%m-%d")), self._meta.get('data_geracao').get('tamanho'))
            return datetime.now().strftime("%Y%m%d")
        if key == "hora_geracao":
            print(len(datetime.now().strftime("%H%I%S")), self._meta.get('hora_geracao').get('tamanho'))
            return datetime.now().strftime("%H%I%S")
        return super().get_value(key, default)

class RegistroBB(Registro0):
    _meta = {
        "codigo_banco": {
            # 01.0
            "tamanho": 3,
            "default": "001",
            "tipo": "int",
            "required": True,
        },
        "codigo_lote": {
            # 02.0
            "tamanho": 4,
            "default": "0000",
            "tipo": "int",
            "required": True,
        },
        "tipo_registro": {
            # 03.0
            "tamanho": 1,
            "default": "0",
            "tipo": "int",
            "required": True,
        },
        "filler1": {
            # 04.0
            "tamanho": 9,
            "default": " ",
            "tipo": "alfa",
            "required": True,
        },
        "tipo_inscricao": {  # 05.0
            "tamanho": 1,
            "default": "0",
            "tipo": "int",
            "required": True,
        },
        "numero_inscricao": {  # 06.0
            "tamanho": 14,
            "default": "0",
            "tipo": "int",
            "required": True,
        },
        "uso_bb1": {  # 07.0
            "tamanho": 20,
            "default": " ",
            "tipo": "alfa",
            "required": True,
        },
        "agencia": {  # 08.0
            "tamanho": 5,
            "default": "0",
            "tipo": "int",
            "required": True,
        },
        "agencia_dv": {  # 09.0
            "tamanho": 1,
            "default": "",
            "tipo": "alfa",
            "required": True,
        },
        "conta": {  # 10.0
            "tamanho": 12,
            "default": "0",
            "tipo": "int",
            "required": True,
        },
        "conta_dv": {  # 11.0
            "tamanho": 1,
            "default": "0",
            "tipo": "alfa",
            "required": True,
        },
        "filler2": {  # 12.0
            "tamanho": 1,
            "default": " ",
            "tipo": "alfa",
            "required": True,
        },
        "nome_empresa": {  # 13.0
            "tamanho": 30,
            "default": "",
            "tipo": "alfa",
            "required": True,
        },
        "nome_banco": {  # 14.0
            "tamanho": 30,
            "default": "BANCO DO BRASIL S.A",
            "tipo": "alfa",
            "required": True,
        },
        "filler3": {  # 15.0
            "tamanho": 10,
            "default": " ",
            "tipo": "alfa",
            "required": True,
        },
        "codigo_remessa": {  # 16.0
            "tamanho": 1,
            "default": "1",
            "tipo": "int",
            "required": True,
        },
        "data_geracao": {  # 17.0
            "tamanho": 8,
            "default": "",  # nao informar a data na instanciaÃ§Ã£o - gerada dinamicamente
            "tipo": "date",
            "required": True,
        },
        "hora_geracao": {  # 18.00
            "tamanho": 6,
            "default": "",  # nao informar a data na instanciaÃ§Ã£o - gerada dinamicamente
            "tipo": "int",
            "required": True,
        },
        "numero_sequencial_arquivo": {  # 19.0
            "tamanho": 6,
            "default": "0",
            "tipo": "int",
            "required": True,
        },
        "versao_layout": {  # 20.0
            "tamanho": 3,
            "default": "000",
            "tipo": "int",
            "required": True,
        },
        "densidade_gravacao": {  # 21.0
            "tamanho": 5,
            "default": "0",
            "tipo": "int",
            "required": True,
        },
        "filler4": {  # 22.0
            "tamanho": 20,
            "default": " ",
            "tipo": "alfa",
            "required": True,
        },
        "situacao_arquivo2": {  # 23.0
            "tamanho": 20,
            "default": " ",
            "tipo": "alfa",
            "required": True,
        },
        "filler5": {"tamanho": 14, "default": " ", "tipo": "alfa", "required": True},
        "filler6": {  # Caso a versão do leiaute seja 30,
            "tamanho": 3,  # Deve ser preenchido com 'zeros' nas posições 226 a 228.
            "default": "000",
            "tipo": "alfa",
            "required": True,
        },
        "filler7": {"tamanho": 12, "default": " ", "tipo": "alfa", "required": True},
    }

"""
ctb = Santander240Header(
    nome_empresa="Empresa ABC",
    tipo_inscricao=2,
    numero_inscricao="70116028106",
    agencia=1234,
    agencia_dv=1,
    conta=12345,
    conta_dv=1,
    codigo_beneficiario=123456,
    numero_sequencial_arquivo=1
)
ctb.get_text()
