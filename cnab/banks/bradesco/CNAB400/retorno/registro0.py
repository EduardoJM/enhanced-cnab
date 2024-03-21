from cnab.base.retorno.CNAB400 import Registro0Retorno
from cnab.core.field import CNABField, CNABFieldType
from .registro1 import BradescoRetornoCnab400Registro1
from .registro4 import BradescoRetornoCnab400Registro4

class BradescoRetornoCnab400Registro0(Registro0Retorno):
    registro1_class = BradescoRetornoCnab400Registro1
    _meta = {
        'tipo_registro': CNABField(
            length=1,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'operacao': CNABField(
            length=1,
            default='2',
            validation=CNABFieldType.Int,
            required=True),
        'literal_retorno': CNABField(
            length=7,
            default='RETORNO',
            validation=CNABFieldType.Alfa,
            required=True),
        'tipo_servico': CNABField(
            length=2,
            default='01',
            validation=CNABFieldType.Int,
            required=True),
        'literal_servico': CNABField(
            length=15,
            default='COBRANCA',
            validation=CNABFieldType.Alfa,
            required=True),
        'codigo_empresa': CNABField(
            length=20,
            default='',
            validation=CNABFieldType.Alfa,
            required=True),
        'nome_empresa': CNABField(
            length=30,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'codigo_banco': CNABField(
            length=3,
            default='237',
            validation=CNABFieldType.Int,
            required=True),
        'nome_banco': CNABField(
            length=15,
            default='BRADESCO',
            validation=CNABFieldType.Alfa,
            required=True),
        'data_gravacao': CNABField(
            length=6,
            default='',# nao informar a data na instanciaÃ§Ã£o - gerada dinamicamente
            validation=CNABFieldType.Date,
            required=True),
        'densidade_gravacao': CNABField(
            length=8,
            default='0',
            validation=CNABFieldType.Int,
            required=True),
        'n_aviso_bancario': CNABField(
            length=5,
            default='',
            validation=CNABFieldType.Int,
            required=True),
        'filler1': CNABField(
            length=266,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'data_credito': CNABField(
            length=6,
            default='',# nao informar a data na instanciaÃ§Ã£o - gerada dinamicamente
            validation=CNABFieldType.Date,
            required=True),
        'filler2': CNABField(
            length=9,
            default=' ',
            validation=CNABFieldType.Alfa,
            required=True),
        'numero_sequencial_registro': CNABField(
            length=6,
            default='',
            validation=CNABFieldType.Int,
            required=True),
    }

    @property
    def has_pix(self):
        return "qrpix.bradesco.com.br" in self.file._lines[2]
    
    def _parse_pix_child_item(self):
        line = self.file._lines[self.file._lines_counter]
        instance = BradescoRetornoCnab400Registro4(self.file, line)
        self.children.append(instance)

    def _parse_childs(self):
        diff = 3 if self.has_pix else 2

        while (self.file._lines_counter < len(self.file._lines) - diff):
            self._parse_child_item()
            self._parse_pix_child_item()
