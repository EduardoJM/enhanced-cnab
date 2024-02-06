from typing import Optional, Union, TYPE_CHECKING
from cnab.base.cnab_240 import CNAB240Registro1
from cnab.core.field import CNABField, CNABFieldType
from cnab.utils.dict_utils import set_if_has_value
from .registro5 import BancoBrasil240Registro5

if TYPE_CHECKING:
    from .registro0 import BancoBrasil240Registro0

class BancoBrasil240Registro1(CNAB240Registro1):
    registro5_class = BancoBrasil240Registro5
    _meta = {
        "codigo_banco": CNABField(  # 01.1
            length=3, default="001", validation=CNABFieldType.Int, required=True
        ),
        "codigo_lote": CNABField(  # 02.1
            length=4, default=1, validation=CNABFieldType.Int, required=True
        ),
        "tipo_registro": CNABField(  # 3.1
            length=1, default=1, validation=CNABFieldType.Int, required=True
        ),
        "operacao": CNABField(  # 04.1
            length=1, default="R", validation=CNABFieldType.Alfa, required=True
        ),
        "tipo_servico": CNABField(  # 05.1
            length=2, default="01", validation=CNABFieldType.Int, required=True
        ),
        "filler1": CNABField(  # 06.1
            length=2, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "versa_layout": CNABField(  # 07.1
            length=3, default="000", validation=CNABFieldType.Int, required=True
        ),
        "filler2": CNABField(  # 08.1
            length=1, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "tipo_inscricao": CNABField(  # 09.1
            length=1, default="0", validation=CNABFieldType.Int, required=True
        ),
        "numero_inscricao": CNABField(  # 10.1
            length=15, default="", validation=CNABFieldType.Int, required=True
        ),
        "convenio": CNABField(  # 11.1
            length=9, default="0", validation=CNABFieldType.Int, required=True
        ),
        "cobranca": CNABField(  # 11.1
            length=4, default="0014", validation=CNABFieldType.Int, required=True
        ),
        "carteira": CNABField(  # 11.1
            length=2, default="0", validation=CNABFieldType.Int, required=True
        ),
        "variacao": CNABField(  # 11.1
            length=3, default="000", validation=CNABFieldType.Int, required=True
        ),
        "situacao_arquivo": CNABField(  # 11.1
            length=2, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "agencia": CNABField(  # 12.1
            length=5, default="", validation=CNABFieldType.Int, required=True
        ),
        "agencia_dv": CNABField(  # 13.1
            length=1, default="", validation=CNABFieldType.Alfa, required=True
        ),
        "conta": CNABField(  # 14.1
            length=12, default="", validation=CNABFieldType.Int, required=True
        ),
        "conta_dv": CNABField(  # 15.1
            length=1, default="", validation=CNABFieldType.Alfa, required=True
        ),
        "filler3": CNABField(  # 16.1
            length=1, default="0", validation=CNABFieldType.Alfa, required=True
        ),
        "nome_empresa": CNABField(  # 17.1
            length=30, default="", validation=CNABFieldType.Alfa, required=True
        ),
        "mensagem_fixa1": CNABField(  # 18.1 mensagems 1 e 2 : somente use para mensagens que serao impressas de forma identica em todos os boletos do lote
            length=40, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "mensagem_fixa2": CNABField(  # 19.1 mensagems 1 e 2 : somente use para mensagens que serao impressas de forma identica em todos os boletos do lote
            length=40, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "numero_remessa": CNABField(  # 20.1
            length=8, default="0", validation=CNABFieldType.Int, required=True
        ),
        "data_gravacao": CNABField(  # 21.1
            length=8,
            default="",  # nao informar a data na instanciação - gerada dinamicamente
            validation=CNABFieldType.Date,
            required=True,
        ),
        "filler4": CNABField(  # 22.1
            length=8, default="0", validation=CNABFieldType.Int, required=True
        ),
        "filler5": CNABField(  # 23.1
            length=33, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
    }

    def __init__(
        self,
        header: "BancoBrasil240Registro0",
        parent: "BancoBrasil240Registro0",
        *,
        codigo_banco: Optional[Union[str, int]] = None,
        codigo_lote: Optional[Union[str, int]] = None,
        tipo_registro: Optional[Union[str, int]] = None,
        operacao: Optional[Union[str, int]] = None,
        tipo_servico: Optional[Union[str, int]] = None,
        tipo_inscricao: Optional[Union[str, int]] = None,
        numero_inscricao: Optional[Union[str, int]] = None,
        convenio: Optional[Union[str, int]] = None,
        cobranca: Optional[Union[str, int]] = None,
        carteira: Optional[Union[str, int]] = None,
        variacao: Optional[Union[str, int]] = None,
        agencia: Optional[Union[str, int]] = None,
        agencia_dv: Optional[Union[str, int]] = None,
        conta: Optional[Union[str, int]] = None,
        conta_dv: Optional[Union[str, int]] = None,
        nome_empresa: Optional[str] = None,
        mensagem_fixa1: Optional[str] = None,
        mensagem_fixa2: Optional[str] = None,
        numero_remessa: Optional[Union[str, int]] = None,
        **kwargs: dict,
    ):
        set_if_has_value(kwargs, 'codigo_banco', codigo_banco)
        set_if_has_value(kwargs, 'codigo_lote', codigo_lote)
        set_if_has_value(kwargs, 'tipo_registro', tipo_registro)
        set_if_has_value(kwargs, 'operacao', operacao)
        set_if_has_value(kwargs, 'tipo_servico', tipo_servico)
        set_if_has_value(kwargs, 'tipo_inscricao', tipo_inscricao)
        set_if_has_value(kwargs, 'numero_inscricao', numero_inscricao)
        set_if_has_value(kwargs, 'convenio', convenio)
        set_if_has_value(kwargs, 'cobranca', cobranca)
        set_if_has_value(kwargs, 'carteira', carteira)
        set_if_has_value(kwargs, 'variacao', variacao)
        set_if_has_value(kwargs, 'agencia', agencia)
        set_if_has_value(kwargs, 'agencia_dv', agencia_dv)
        set_if_has_value(kwargs, 'conta', conta)
        set_if_has_value(kwargs, 'conta_dv', conta_dv)
        set_if_has_value(kwargs, 'nome_empresa', nome_empresa)
        set_if_has_value(kwargs, 'mensagem_fixa1', mensagem_fixa1)
        set_if_has_value(kwargs, 'mensagem_fixa2', mensagem_fixa2)
        set_if_has_value(kwargs, 'numero_remessa', numero_remessa)
        super().__init__(header, parent, **kwargs)

    def inserir_detalhe(self, **kwargs):
        from .registro3P import BancoBrasil240Registro3P
        return BancoBrasil240Registro3P(self.header, self, self, **kwargs)
