from abc import ABC
from enum import Enum
from typing import TYPE_CHECKING, List

from .exceptions import RetornoEmptyFile, RetornoInvalidLineLength

if TYPE_CHECKING:
    from .registro_retorno import RegistroRetorno


class RetornoLayoutType(Enum):
    CNAB400 = "400"
    CNAB240 = "240"


class Retorno(ABC):
    registro0_class = None
    registro9_class = None

    _lote_counter = 1
    _lines_counter = 0
    _content: str = ""
    _lines: List[str] = []
    _layout: RetornoLayoutType

    children: List["RegistroRetorno"] = []

    def _initialize_content(self, content: str):
        self._content = content.replace("\r\n", "\n")
        self._lines = self._content.split("\n")
        self._lines = list(filter(lambda f: bool(f), self._lines))
        if len(self._lines) < 2:
            raise RetornoEmptyFile()

    def _validate_file(self):
        # TODO: automatic identify the file layout inside the 240's cnab's?

        length = len(self._lines[0])
        if length == 240:
            self._layout = RetornoLayoutType.CNAB240
        elif length == 400:
            self._layout = RetornoLayoutType.CNAB400
        else:
            raise RetornoInvalidLineLength(length)

    def _parse_file(self):
        instance = self.registro0_class(self, self._lines[0])
        self.children.append(instance)

        instance = self.registro9_class(self, self._lines[-1])
        self.children.append(instance)

    def __init__(self, content: str):
        self._lote_counter = 1
        self._lines_counter = 0
        self.children = []

        self._initialize_content(content)
        self._validate_file()
        self._parse_file()
