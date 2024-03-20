from cnab.base.retorno.registro_retorno import RegistroRetorno
from cnab.base.retorno.retorno import Retorno

class Registro0Retorno(RegistroRetorno):
    registro1_class = None
    
    def _parse_child_item(self):
        line = self.file._lines[self.file._lines_counter]
        instance = self.registro1_class(self.file, line)
        self.children.append(instance)

    def _parse_childs(self):
        while (self.file._lines_counter < len(self.file._lines) - 2):
            self._parse_child_item()

    def __init__(self, file: Retorno, line: str):
        super().__init__(file, line)
        self.file._lines_counter += 1
        self._parse_childs()
