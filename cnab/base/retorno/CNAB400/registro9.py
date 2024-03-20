from cnab.base.retorno.registro_retorno import RegistroRetorno
from cnab.base.retorno.retorno import Retorno

class Registro9Retorno(RegistroRetorno):
    def __init__(self, file: Retorno, line: str):
        super().__init__(file, line)
        self.file._lines_counter += 1
