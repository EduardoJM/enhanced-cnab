from .registro_base import RegistroBase

class RegistroRemessa(RegistroBase):
    def get_text(self) -> str:
        retorno = ''
        for key, field in self._meta.items():
            #print(key, field)
            #print(self.get_value(key, field.default))
            retorno += self.get_value(key, field.default)
            
        #print("___________________")
        #print(retorno)
        #print("___________________")
        #print(len(retorno))

        # TODO: work with childs
            
        result = [retorno]
        
        print(self._children)

        for child in self._children:
            result += child.get_text()

        return result
