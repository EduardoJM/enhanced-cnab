from .registro import Registro

class RegistroRemessa(Registro):
    def get_text(self) -> str:
        retorno = ''
        for key, field in self._meta.items():
            #field.registro = self
            #default = self.get_default(field)
            retorno += field.get_value()
            
        result = [retorno]

        for child in self._children:
            result += child.get_text()

        return result
