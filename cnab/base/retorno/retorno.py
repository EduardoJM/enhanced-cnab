from typing import List
from enum import Enum
from abc import ABC
from .exceptions import (
    RetornoEmptyFile,
    RetornoInvalidLineLength,
)

class RetornoLayoutType(Enum):
    CNAB400 = '400'
    CNAB240 = '240'

class Retorno(ABC):
    registro0_class = None

    _lote_counter = 1
    _lines_counter = 0
    _content: str = ""
    _lines: List[str] = []
    _layout: RetornoLayoutType

    def _initialize_content(self, content: str):
        self._content  = content.replace("\r\n", "\n")
        self._lines = self._content.split('\n')
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
        pass

    def __init__(self, content: str):
        self._lote_counter = 1
        self._lines_counter = 0

        self._initialize_content(content)
        self._validate_file()
        self._parse_file()
