from .registro import Registro

class RegistroRemessa(Registro):
    def get_text(self) -> str:
        retorno = ''
        for key, field in self._meta.items():
            retorno += self.get_value(key, field.default)
            
        result = [retorno]

        for child in self._children:
            result += child.get_text()

        return result
