import re
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from .remessa import Remessa

class Registro:
    _children: List["Remessa"] = []
    _meta: Optional[dict] = None
    _data: Optional[dict] = None

    def __init__(self, **kwargs: dict):
        self._data = kwargs

    def remove_accents(self, text):
        regexes = [
            r'\xc3[\x80-\x85]',
            r'\xc3\x87',
            r'\xc3[\x88-\x8b]',
            r'\xc3[\x8c-\x8f]',
            r'\xc3([\x92-\x96]|\x98)',
            r'\xc3[\x99-\x9c]',
            r'\xc3[\xa0-\xa5]',
            r'\xc3\xa7',
            r'\xc3[\xa8-\xab]',
            r'\xc3[\xac-\xaf]',
            r'\xc3([\xb2-\xb6]|\xb8)',
            r'\xc3[\xb9-\xbc]'
        ]
        replacers = ['A', 'C', 'E', 'I', 'O', 'U', 'a', 'c', 'e', 'i', 'o', 'u']
        for regex, repl in zip(regexes, replacers):
            text = re.sub(regex, repl, text).lower()
        return text

    def prepare_text(self, text: str):
        return self.remove_accents(text.strip()).upper()

    def get_value(self, key, default):
        value = self._data.get(key, default)
        
        meta_data = self._meta.get(key)
        if meta_data.get('required') and not value:
            msg = f"Campo faltante ou com valor nulo: {key}"
            if self._data.get('nosso_numero'):
                msg = f"{msg}. Boleto Numero: {self._data.get('nosso_numero')}"
            # TODO: create custom exception here
            raise Exception(msg)
        
        if meta_data['tipo'] == 'int':
            print(len(str(int(value)).rjust(meta_data.get('tamanho'), '0')), meta_data.get('tamanho'))
            return str(int(value)).rjust(meta_data.get('tamanho'), '0')
        if meta_data['tipo'] == 'alfa':
            value = self.prepare_text(str(value))
            if len(value) > meta_data.get('tamanho'):
                value = value[0:meta_data.get('tamanho')]
            print(len(value.ljust(meta_data.get('tamanho', '0'))), meta_data.get('tamanho'))
            return value.ljust(meta_data.get('tamanho', '0'))
                
        return value

    def append(self, child: "Remessa"):
        self._children.append(child)

    def get_text(self) -> str:
        raise NotImplementedError("get_text() is not implemented")

class RegistroRem(Registro):
    def get_text(self) -> str:
        retorno = ''
        for key, value in self._meta.items():
            print(key, value)
            retorno += self.get_value(key, value.get('default'))
            
        print("___________________")
        print(retorno)
        print("___________________")
        print(len(retorno))
        for child in self._children:
            child.get_text()

